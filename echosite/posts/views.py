from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from typing import Optional
from echosite.settings import BASE_DIR
import os
import uuid
import boto3
import json
import datetime
from .models import Post, User
from django.core.serializers import serialize

# Create SQS client
sqs = boto3.client('sqs')
pending_queue_url = os.environ['SQS_PENDING_URL']

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")

def generate_post(request):
    topics = ''.join(request.POST['topics'])
    
    # Send message to SQS queue
    post_id = str(uuid.uuid4())
    message = {
        'topics': topics,
        'author_id': request.user.id,
        'post_id': post_id,
    }
    message_json = json.dumps(message)
    response = sqs.send_message(
        QueueUrl=pending_queue_url,
        MessageBody=message_json,
        MessageGroupId='dummy',
        MessageDeduplicationId=post_id
    )
    print(response)

    return JsonResponse({'prompt': 'Post generation in-progress! Check back later :)'})

def consume_posts(request):
    # Create SQS client
    consumed_msgs = 0
    sqs = boto3.client('sqs')
    completed_queue_url = os.environ['SQS_COMPLETED_URL']
    response = sqs.receive_message(
        AttributeNames=['CreatedTimestamp'],
        MessageAttributeNames=[
            'All',
        ],
        QueueUrl=completed_queue_url,
        MaxNumberOfMessages=10,
        VisibilityTimeout=300,
        WaitTimeSeconds=10
    )

    try:
        messages = response['Messages']
        consumed_msgs = len(messages)
        for message in messages:
            receipt_handle = message['ReceiptHandle']

            body_json = message['Body']
            body = json.loads(body_json)
            topics = body['topics']
            author_id = body['author_id']
            post_id = body['post_id']
            post_text = body['post']
            timestamp = body['timestamp']
            datetime_object = datetime.datetime.fromtimestamp(timestamp / 1000000, tz=datetime.timezone.utc)

            print('Received: {}, {}, {}, {}'.format(author_id, post_id, topics, post_text))

            # Add to DB
            new_post = Post()
            author = User.objects.get_or_create(pk=author_id)
            new_post.author = author[0]
            new_post.post_id = post_id
            new_post.timestamp = datetime_object
            new_post.post_text = post_text
            new_post.save()

            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=completed_queue_url,
                ReceiptHandle=receipt_handle
            )
    except Exception as e:
        print('No messages?: {}, {}'.format(e, response))
        pass
    return HttpResponse('Consumed {} messages'.format(consumed_msgs))

# Returns latest N posts (make configurable in GET)
def get_posts(request):
    recent_100_posts = Post.objects.all()[:100]
    print(recent_100_posts)
    serialized_data = serialize("json", recent_100_posts)
    return HttpResponse(serialized_data)
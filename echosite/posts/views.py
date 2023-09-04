from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from typing import Optional
from echosite.settings import BASE_DIR
import os
import uuid
import boto3
import json

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
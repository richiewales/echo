import os
from datetime import datetime
import boto3
import uuid
import boto3
import json
import time
from llama_cpp import Llama
from sys import platform

model_dir = 'Llama-2-7B-Chat-GGML'
model_file = 'llama-2-7b-chat.ggmlv3.q4_0.bin'
n_gpu_layers = 0

if platform == 'darwin':
    n_gpu_layers = 1

# Create SQS client
sqs = boto3.client('sqs')
pending_queue_url = os.environ['SQS_PENDING_URL']
completed_queue_url = os.environ['SQS_COMPLETED_URL']

# Infinite loop to process SQS messages
while True:
    response = sqs.receive_message(
        AttributeNames=['CreatedTimestamp'],
        MessageAttributeNames=[
            'All',
        ],
        QueueUrl=pending_queue_url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=300,
        WaitTimeSeconds=10
    )

    try:
        messages = response['Messages']
        for message in messages:
            receipt_handle = message['ReceiptHandle']

            body_json = message['Body']
            body = json.loads(body_json)
            topics = body['topics']
            author_id = body['author_id']
            post_id = body['post_id']

            print('Received: {}, {}, {}'.format(author_id, post_id, topics))
            llm = Llama(model_path=os.path.join('models', model_dir, model_file), n_gpu_layers=n_gpu_layers)
            output = llm("Q: Generate a tweet about {}.  A: ".format(topics), max_tokens=128, stop=["Q:", "\n"], echo=True)
            output = output['choices'][0]['text'].split('A: ')[1]
            print('Generated: {}'.format(output))

            # Send output to completed queue
            # Send message to SQS queue
            completed_message = {
                'topics': topics,
                'author_id': author_id,
                'post_id': post_id,
                'post': output,
                'timestamp': int(datetime.utcnow().timestamp()*1e3),
            }
            completed_message_json = json.dumps(completed_message)
            response = sqs.send_message(
                QueueUrl=completed_queue_url,
                MessageBody=completed_message_json,
                MessageGroupId=post_id,
                MessageDeduplicationId=post_id
            )
            print(response)

            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=pending_queue_url,
                ReceiptHandle=receipt_handle
            )
    except Exception as e:
        print('No messages?: {}, {}'.format(e, response))
        pass
    time.sleep(15)
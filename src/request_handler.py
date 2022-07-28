import boto3
import json
import os

sqs = boto3.client('sqs')
sqs_url = os.environ['SQS_QUEUE_URL']
def request_handler(event, context):
    sqs.send_message(
        QueueUrl=sqs_url,
        MessageBody=json.dumps(event)
    )

    return ('Messaged Received', 200)
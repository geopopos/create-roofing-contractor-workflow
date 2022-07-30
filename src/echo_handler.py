import json

def echo_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
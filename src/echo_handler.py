import json, os

def echo_handler(event, context):

    print(os.environ.get("WORKFLOW_FILE"))
    return {
        'statusCode': 200,
        'body': json.dumps(event),
        'email': event.get('email')
    }
import json, requests, os

ppl_api_url ="https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_OFFLINE'):
    ppl_api_url = "http://localhost:2000"

def add_stripe_customer_dynamo(event, context):
    stripe_id = event.get('stripe_id')
    roofer_id = event.get('roofer_id')

    

    body = {
        "StripeId": stripe_id
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.request("PUT", ppl_api_url, headers=headers, data=json.dumps(body))

    response_body = json.loads(response.text)
    breakpoint()

    # Return data for use in future steps
    export("stripe_id", stripe_id)
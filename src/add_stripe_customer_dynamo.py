import json, requests, os
from urllib import parse

ppl_api_url ="https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_LOCAL') == 'true':
    ppl_api_url = "http://localhost:2000"

def add_stripe_customer_dynamo(event, context):
    stripe_id = event.get('stripe_customer_id')
    roofer_id = event.get('roofer_id')

    update_roofer_url = f"{ppl_api_url}/roofer/{parse.quote(roofer_id)}"
    

    body = {
        "StripeId": stripe_id
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.request("PUT", update_roofer_url, headers=headers, data=json.dumps(body))

    response_body = json.loads(response.text)

    output_json = {
        "stripe_customer_id": stripe_id,
        "name": event.get('name'),
        "phone": event.get('phone'),
        "roofer_id": event.get('roofer_id')
    }
    # Return data for use in future steps
    return output_json
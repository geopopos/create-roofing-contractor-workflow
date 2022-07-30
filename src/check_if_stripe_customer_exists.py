import json, stripe, requests, os

# uncomment the following line to run in production with live stripe key
# stripe_api_key = os.environ.get('STRIPE_API_KEY')
# 
# if os.environ.get('IS_OFFLINE'):
#     stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')
# 

stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')

def check_if_stripe_customer_exists(event, context):
    print(event)
    event_body = event.get('Records')[0].get('body')
    customer_email = event_body.get('email')
    print("customer_email: " + customer_email)
    # customer_name = event.get('name')
    # customer_phone = event.get('phone')
    # customer_roofer_id = event.get('roofer_id')

    stripe.api_key = stripe_api_key

    response = stripe.Customer.list(email=customer_email, limit=1)
    return json.loads(response.text)

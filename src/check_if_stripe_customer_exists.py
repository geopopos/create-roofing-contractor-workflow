import json, stripe, requests, os

stripe_api_key = os.environ.get('STRIPE_API_KEY')

if os.environ.get('IS_OFFLINE'):
    stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')

def check_if_stripe_customer_exists(event, context):
    customer_email = event.get('email')
    customer_name = event.get('name')
    customer_phone = event.get('phone')
    customer_roofer_id = event.get('roofer_id')

    response = stripe.Customer.list(email=customer_email, limit=1)
    return response['data'], 200

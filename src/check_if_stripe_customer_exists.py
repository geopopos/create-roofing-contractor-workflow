import json, stripe, requests, os

stripe_api_key = os.environ.get('STRIPE_API_KEY')

if os.environ.get('IS_LOCAL') or os.environ.get('STAGE') == 'dev':
    stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')

def check_if_stripe_customer_exists(event, context):
    print(event)
    customer_email = event.get('email')
    print("customer_email: " + customer_email)
    # customer_name = event.get('name')
    # customer_phone = event.get('phone')
    # customer_roofer_id = event.get('roofer_id')

    stripe.api_key = stripe_api_key

    response = stripe.Customer.list(email=customer_email, limit=1)
    if response['data']:
        return {
            'statusCode': 200,
            'stripeCustomerExists': True,
            'data': response['data'],
            'email': customer_email,
            'phone': event.get('phone'),
            'name': event.get('name'),
            'roofer_id': event.get('pk')
        } 
    else:
        return {
            'statusCode': 404,
            'stripeCustomerExists': False,
            'data': response['data'],
            'email': customer_email,
            'phone': event.get('phone'),
            'name': event.get('name'),
            'roofer_id': event.get('pk')
        }

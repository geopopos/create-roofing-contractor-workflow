import json, stripe, requests, os

stripe_api_key = os.environ.get('STRIPE_API_KEY')

if os.environ.get('IS_LOCAL') or os.environ.get('STAGE') == 'dev':
    stripe_api_key = os.environ.get('STRIPE_TEST_API_KEY')

def create_stripe_customer(event, context):
    print(event)
    customer_email = event.get('email')
    customer_phone = event.get('phone')
    customer_name = event.get('name')
    customer_roofer_id = event.get('roofer_id')

    stripe.api_key = stripe_api_key

    stripe_customer = stripe.Customer.create(
        email=customer_email,
        metadata={
          "roofer_id": customer_roofer_id,
        },
        phone=customer_phone,
        name=customer_name
    )
    output_object = {
        "stripe_customer_id": stripe_customer['id'],
        "roofer_id": customer_roofer_id,
        "name": customer_name,
        "phone": customer_phone
    }
    
    return output_object

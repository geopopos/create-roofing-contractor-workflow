import json, requests, os

ppl_api_url ="https://e6b1hc9rfg.execute-api.us-east-1.amazonaws.com"

if os.environ.get('IS_OFFLINE'):
    ppl_api_url = "http://localhost:2000"


def create_roofing_contractor(event, context):
    email = event.get('email')
    first_name = event.get('first_name') 
    last_name = event.get('last_name')
    phone = event.get('phone')
    url = f"{ppl_api_url}/roofer"
    payload = {
        "First Name": first_name,
        "Last Name": last_name,
        "Phone": phone,
        "Email": email
    }
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return json.loads(response.text)
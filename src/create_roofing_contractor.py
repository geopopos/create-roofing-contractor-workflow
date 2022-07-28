import json, requests

def create_roofing_contractor(event, context):
    email = event.get('email')
    first_name = event.get('first_name') 
    last_name = event.get('last_name')
    phone = event.get('phone')
    url = "http://localhost:2000/roofer"
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
    return response.text
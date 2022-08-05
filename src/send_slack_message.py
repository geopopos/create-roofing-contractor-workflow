import requests, json

# send a public channel message in slack
def send_slack_message(event, context):
    pipe_dream_url = "https://eouzz6hggmlx2kz.m.pipedream.net"
    headers = {
        "Content-Type": "application/json"
    }
    body = json.dumps(event) 
    breakpoint()
    requests.request("POST", pipe_dream_url, headers=headers, data=body)
    return {"statusCode": 200}



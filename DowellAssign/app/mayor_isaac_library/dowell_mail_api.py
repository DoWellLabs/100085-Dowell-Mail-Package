import requests
import json

def send_email(api_key, to_email, to_name, from_name, from_email, subject, body):

    url = f"https://100085.pythonanywhere.com/api/v1/mail/{api_key}/?type=send-email"

    payload = json.dumps({
    "email": to_email,
    "name": to_name,
    "fromName": from_name,
    "fromEmail": from_email,
    "subject": subject,
    "body": body
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def validate_mail(api_key, to_email, to_name, from_name, from_email, subject, body):
    url = f"https://100085.pythonanywhere.com/api/v1/mail/{api_key}/?type=validate"

    payload = json.dumps({
    "email": to_email,
    "name": to_name,
    "fromName": from_name,
    "fromEmail": from_email,
    "subject": subject,
    "body": body
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None




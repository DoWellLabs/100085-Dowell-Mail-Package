from django.shortcuts import render
import requests
import json
from django.contrib import messages
import os
from dotenv import load_dotenv

load_dotenv()


def home(request):
    if request.method== "POST":

        api_key = os.getenv('API_KEY')
        toEmail = request.POST.get('toEmail')
        body = {
            "email": toEmail,
            "name":request.POST.get('fullName'),
            "fromName":request.POST.get('fullName'),
            "fromEmail" : request.POST.get('fromEmail'),
            "subject" : request.POST.get('subject'),
            "body" : request.POST.get('message')
        }

       
        #validate = f'https://100085.pythonanywhere.com/api/v1/mail/{api_key}/?type=validate'
        validate = f'https://100085.pythonanywhere.com/api/v1/mail/e73e9749-99e0-4bfb-b76c-a86d2a7c7d89/?type=validate'
        res = requests.post(validate, json=body)
        validate_response = res.json()
        if validate_response['success'] == True:
            send_mail = f'https://100085.pythonanywhere.com/api/v1/mail/{api_key}/?type=send-email'
            resp = requests.post(send_mail, json=body)
            mail_response = resp.json()
            if mail_response['success'] == True:
                messages.add_message(request, messages.INFO, mail_response['message'])
            else:
                messages.add_message(request, messages.ERROR, mail_response['message'])
        else:
            messages.add_message(request, messages.ERROR, validate_response['message'])
 
    return render(request, 'maillib/home.html')


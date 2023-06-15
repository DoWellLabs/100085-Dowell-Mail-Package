from django.test import Client, TestCase
import requests
import json
from django.urls import reverse
from django.contrib.messages import get_messages
import os
from dotenv import load_dotenv

load_dotenv()


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
    
    def test_should_show_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maillib/home.html")

    def test_email_validate(self):
       response = self.client.post(self.home_url)
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'maillib/home.html')

    def test_valid_email(self):
        data = {
            "email":"marvinwandabwa0@gmail.com",
            "name":"Marvin",
            "fromName":"Marvin Okwaro",
            "fromEmail" : "marvin.wekesa@gmail.com",
            "subject" : "Final mail test",
            "body" : "I am sending as a test mail"
        }
        api_key = os.getenv('API_KEY')
        url = f'https://100085.pythonanywhere.com/api/v1/mail/{api_key}/?type=validate'

        response = requests.post(url, json=data)
        valid_resp = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(valid_resp['success'], True)
        


    def test_send_email(self):
        data = {
            "email":"marvinwandabwa0@gmail.com",
            "name":"Marvin",
            "fromName":"Marvin Okwaro",
            "fromEmail" : "marvin.wekesa@gmail.com",
            "subject" : "Final mail test",
            "body" : "I am sending as a test mail"
        }
        api_key = os.getenv('API_KEY')
        url = f'https://100085.pythonanywhere.com/api/v1/mail/{api_key}/?type=send-email'

        response = requests.post(url, json=data)
        email_resp = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(email_resp['success'], True)
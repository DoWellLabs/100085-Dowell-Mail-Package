from django.test import TestCase
from django.urls import reverse, resolve
from maillib.views import home

class TestUrls(TestCase):
    
    def test_home_url_resolved(self):
        url = reverse('home')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,home)

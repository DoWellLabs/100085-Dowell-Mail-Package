from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.contact_form, name="contactus"),
    path("sendmail", views.send_email_view, name="sendmail"),

]
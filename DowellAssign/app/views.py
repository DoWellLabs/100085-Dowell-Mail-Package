from django.http import HttpResponse, JsonResponse
from django.utils.html import escape

from app.mayor_isaac_library.dowell_mail_api import send_email, validate_mail

from django.contrib import messages

from .secretekeys import API_KEY

from django.shortcuts import render


def contact_form(request):
    if request.method == "POST":
        to_email = escape(request.POST.get("email"))
        to_name = escape(request.POST.get("name"))
        from_name = "Dowell Research"
        from_email = "mdashsharma95@gmail.com"
        subject = "From Contact US page"
        body = escape(request.POST.get("message"))

        api_key = API_KEY

        validate_response = validate_mail(api_key, to_email, to_name, from_name, from_email, subject, body)

        if validate_response['success'] == True:
            response_text = send_email(api_key, to_email, to_name, from_name, from_email, subject, body)

            messages.success(request, "Email sent successfully!")
        else:

            messages.error(request, "Error!")

        return render(request, "index.html")
    else:
        return render(request, "index.html")



def send_email_view(request):
    if request.method == "POST":
        to_email = escape(request.POST.get("to_email"))
        to_name = escape(request.POST.get("to_name"))
        from_name = escape(request.POST.get("from_name"))
        from_email = escape(request.POST.get("from_email"))
        subject = escape(request.POST.get("subject"))
        body = escape(request.POST.get("body"))

        api_key = API_KEY

        validate_response = validate_mail(api_key, to_email, to_name, from_name, from_email, subject, body)

        if validate_response['success'] == True:
            response_text = send_email(api_key, to_email, to_name, from_name, from_email, subject, body)

            messages.success(request, "Email sent successfully!")
        else:
            messages.error(request, "Error!")

        return render(request, "sendmail.html")
    else:
        return render(request, "sendmail.html")




    

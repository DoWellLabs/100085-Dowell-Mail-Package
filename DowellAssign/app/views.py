from django.http import HttpResponse, JsonResponse
from django.utils.html import escape

from app.mayor_isaac_library.dowell_mail_api import send_email, validate_mail

from django.contrib import messages

from .secretekeys import API_KEY

from django.shortcuts import render


def contact_form(request):
    # Extract data from the request.POST. Accept from Users
    #using django.utils.html escape to validate the incoming request for security purpose
    if request.method == "POST":
        to_email = escape(request.POST.get("email"))
        to_name = escape(request.POST.get("name"))
        from_name = "Dowell Research"
        from_email = "mdashsharma95@gmail.com"
        subject = "From Contact US page"
        body = escape(request.POST.get("message"))

        #call to api key from .secretekeys file
        api_key = API_KEY

        #calling the validating function and store resonse in validate_response
        validate_response = validate_mail(api_key, to_email, to_name, from_name, from_email, subject, body)

        #checking if email is valid before sending the mail
        if validate_response['success'] == True:
            #calling the send email function from library to send the mail and store the response in response_text
            response_text = send_email(api_key, to_email, to_name, from_name, from_email, subject, body)

            if response_text['success'] == True: #if message sent successfully return a message
                messages.success(request, "Email sent successfully!")
            else:
                messages.error(request, "Error!")
        else:

            messages.error(request, "Error!")
        #rendering the html page
        return render(request, "index.html")
    else:
        #rendering the html page
        return render(request, "index.html")
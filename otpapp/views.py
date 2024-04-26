from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
import requests
class Home(View):
    def get (self,request):
        return render(request,'input.html')
class Send(View):
    def get(self,request):
        subject = 'Thankyou for contacting me'
        otp = str(random.randint(10000000,99999999))
        print(otp)
        From_mail = settings.EMAIL_HOST_USER
        email=request.GET["t1"]
        mobno="+91"+request.GET["t2"]
        to_list = [email]
        send_mail(subject, otp, From_mail, to_list, fail_silently=False)
        resp = requests.post('https://textbelt.com/text', {
            'phone': '5555555555',
            'message': 'Hello world',
            'key': '9fdcf215113a8cfdcf3cea6c459754a0d99d7012xHtCt5pejds8GOS4QnM9k7Z0I',
        })
        print(resp.json())
        return HttpResponse("mail sent successfully")






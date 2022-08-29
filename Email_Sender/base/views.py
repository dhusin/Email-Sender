from email import message
import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        to_id = request.POST['to']
        subject = request.POST['subject']
        content = request.POST['message']
        from_id = settings.EMAIL_HOST_USER

        send_mail(subject,content,from_id,[to_id] )

        return render(request,'home.html',)

        
    else:
        return render(request,'home.html')



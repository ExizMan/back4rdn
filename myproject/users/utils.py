from django.core.mail import EmailMessage
import random
from django.conf import settings
from .models import User, OneTimePassword
from django.contrib.sites.shortcuts import get_current_site



def send_generated_otp_to_email(email, request):
    subject = "One time passcode for Email verification"
    otp=random.randint(1000, 9999)
    current_site=get_current_site(request).domain

    email_body=f"Hi {email} , ur otp is {otp}"
    from_email=settings.EMAIL_HOST_USER
    otp_obj=OneTimePassword.objects.create(email=email, otp=otp)
    #send the email
    d_email=EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[email])
    d_email.send()


def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()
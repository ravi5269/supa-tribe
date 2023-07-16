import random
from django.conf import settings
from django.core.mail import send_mail
from users.models import User

def send_otp_via_email(self,email):
        subject  = 'your account verification email'
        otp = random.randint(100009,999999)
        message = f"Your otp is {otp}"
        email_from = settings.EMAIL_HOST
        send_mail(subject,message,email_from,[email])
        user_obj = User.objects.get(email=email)
        user_obj.otp = otp
        user_obj.save()
# app/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)

    # Add as many emails as you want in this list
    recipients = [user.email, "nikhilpradhan62@gmail.com", "boatofficial2025@gmail.com"]

    send_mail(
        subject="Welcome!",
        message="Thanks for joining.",
        from_email="tracking@veegeeauto.com",
        recipient_list=recipients,
    )


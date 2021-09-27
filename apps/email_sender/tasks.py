from django.conf import settings
from django.core.mail import EmailMessage

from booking.celery import app



@app.task
def send_info(email):
    message = f"""
    Элек.почта: {email}
    """
    email = EmailMessage(
        "Kurmanbek Booking",
        message, settings.EMAIL_HOST_USER,
        [email],
    )
    email.send(fail_silently=False)

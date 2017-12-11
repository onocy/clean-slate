from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
from twilio.rest import Client

from .models import Event


# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = Client()

@shared_task
def send_sms_reminder(event_id):
    """Send a reminder to a phone using Twilio SMS"""
    try:
        event = Event.objects.get(pk=event.id)
    except Event.DoesNotExist:
        return

    body = 'You have an upcoming deadline for {0} at {1}.'.format(
        event.title,
        event.deadline
    )

    message = client.messages.create(
        body=body,
        to=appointment.phone_number,
        from_=settings.TWILIO_NUMBER,
    )

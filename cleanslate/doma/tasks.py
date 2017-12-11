from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
import twilio
from twilio.rest import Client

from .models import Event

account_sid = "AC3c7a087cae83e671986819994e5cd5c9"
auth_token = "269e1c35ee3f9778732275985fc6c1b5"
client = Client(account_sid, auth_token)

@shared_task
def send_sms_reminder(event_id):
    """Send a reminder to a phone using Twilio SMS"""
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return

    body = 'You have an upcoming deadline for {0} at {1}.'.format(
        event.title,
        event.deadline
    )

    message = client.messages.create(
        body=body,
        # TODO: fill in with a phone number from the db
        # mboneil10's twilio phone number
        to="+14132764806",
        # "magic number" from Twilio tutorial
        from_="+15005550006",
    )

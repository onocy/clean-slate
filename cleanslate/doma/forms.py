from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from .models import User, Home, Review, Forum, Post, Topic, Village, Transaction, Chore, Reminder, Event, Profile

class UserProfileForm(forms.Form):
        phone = forms.CharField(help_text='Enter your phone number')
        yog = forms.CharField(help_text='Enter your graduation date')
        major = forms.CharField()
        status = forms.CharField(help_text='Enter a status for others to view')
        bio = forms.CharField(help_text='Enter a brief description of yourself')
        # smokes = forms.BooleanField(initial=True, help_text='Do you smoke cigarettes?')
        # bedtime = forms.TimeField(help_text='What is your usual sleep-time?')
        # lastSeen = forms.DateField()
        email = forms.EmailField(help_text='Enter your email')
        # pet_allergies = forms.NullBooleanField(help_text='Are you allergic to pets?')

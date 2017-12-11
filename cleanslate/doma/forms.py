from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import User, Home, Review, Forum, Post, Topic, Village, Transaction, Chore, Reminder, Event, Profile

class UserProfileForm(forms.Form):
    phone = forms.CharField(help_text='Enter your phone number')
    yog = forms.CharField(help_text='Enter your graduation date')
    major = forms.CharField()
    status = forms.CharField(help_text='Enter a status for others to view')
    bio = forms.CharField(help_text='Enter a brief description of yourself', widget=forms.Textarea)
    # smokes = forms.BooleanField(initial=True, help_text='Do you smoke cigarettes?')
    # bedtime = forms.TimeField(help_text='What is your usual sleep-time?')
    # lastSeen = forms.DateField()
    email = forms.EmailField(help_text='Enter your email')
    # pet_allergies = forms.NullBooleanField(help_text='Are you allergic to pets?')
    HOMES = []
    for home in Home.objects.all():
        HOMES += [(home.id, home.name)]
    home = forms.ChoiceField(help_text='Which home do you want to be in?', choices=HOMES)

class EditChoreForm(forms.Form):
    deadline = forms.DateField(help_text = 'When is this chore due?')

    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - deadline cannot be in the past'))
        return data

class CreateChoreForm(forms.Form):
    title = forms.CharField(help_text = 'Enter a chore name')
    description = forms.CharField(help_text = 'Enter a description')
    created_on = forms.DateField()
    deadline = forms.DateField(help_text = 'When is this chore due?')

    def clean_title(self):
        data = self.cleaned_data['title']
        # Check title is not longer than 200 characters
        if len(data) > 200:
            raise ValidationError(_('Invalid title - cannot be longer than 200 characters'))
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        # Check description is not longer than 500
        if len(data) > 500:
            raise ValidationError(_('Invalid description - cannot be longer than 500 characters'))
        return data

    def clean_created_on(self):
        data = self.cleaned_data['created_on']
        # Check date is not in future.
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - created_on cannot be in the future'))
        return data

    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - deadline cannot be in the past'))
        return data

class CreateUserForm(forms.Form):
    username = forms.CharField(help_text = 'Enter a username')
    email = forms.EmailField(help_text = 'Enter an email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User

class CreateHomeForm(forms.Form):
    name = forms.CharField(max_length=100, help_text='Enter your Home Name')
    address = forms.CharField(max_length=100, help_text='Enter your Address')
    leaseStart = forms.DateField()
    leaseEnds = forms.DateField()

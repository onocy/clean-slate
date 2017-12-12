from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import EditProfileForm, EditChoreForm, CreateChoreForm, CreateUserForm, CreateHomeForm, EditUserForm
from doma.models import User, Profile, Home, Review, Forum, Post, Topic, Village, Transaction, Chore, Reminder, Event
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.db import IntegrityError
import datetime

@login_required
def home(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects, this is how you send data to the view...

    # num_users = User.objects.all().count()
    # num_villages = Village.objects.all().count()
    # num_posts = Post.objects.all().count()
    num_topics = Topic.objects.all().count()
    # num_reviews = Review.objects.all().count()


    # Things that are needed on the homepage
    # Name, picture (filler for now) status and last seen fields of user. So we will pass in user
    # in the future, when the application supports multiple users, we will need to
    # filter which users we are showing on the home page based on their home value
    # showing only the ones who share a home with the user currently logged in
    # however, for now, we will show all users on the home page
    # users = User.objects.filter(home__exact=
    from itertools import zip_longest
    def grouper(iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)
    user_groups = list(grouper(Profile.objects.filter(home = request.user.profile.home), 4))

    # Render the HTML template home.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'num_topics': num_topics, 'user_groups': user_groups}
    )

@login_required
def profile(request):
    """
    View function for individual profiles on site.
    """
    if request.user.is_authenticated:
        chosen_user = User.objects.get(pk=request.user.id)

        status = chosen_user.profile.status
        lastSeen = chosen_user.profile.lastSeen
        bio = chosen_user.profile.bio
        email = chosen_user.email
        return render(
            request,
            'profile.html',
                context = {
                'username' : chosen_user.username,
                'status' : status,
                'bio': bio,
                'email': email,
                'lastSeen': lastSeen,
            }
        )
    else:
        return render(
            request,
            'profile.html',
                context = {
                'username': "anonymous",
                'status': "Online",
                'bio': "This user has no bio",
                'email': ""
                }
        )

    return render(
        request,
        'profile.html',
        context={}
    )

@login_required
def calendar(request):
    """
    View function for Calendar
    """
    events = Event.objects.all()

    return render(
        request,
        'calendar.html',
        context={'events': events}
    )

@login_required
def reminders(request):
    """
    View function for reminders (Later- not a separate page)
    """

    events = Event.objects.all()
    transactions = Transaction.objects.all()
    chores = Chore.objects.all()

    return render(
        request,
        'reminders_list.html',
        context={
                'events': events,
                'transactions':transactions,
                'chores':chores
            }
    )

@login_required
def finance(request):
    """
    View function for reminders (Later- not a separate page)
    """
    finance = Transaction.objects.all()
    return render(
        request,
        'finance_list.html',
            context={
                'transactions': finance
            }
    )

@login_required
def edit_user_profile(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    new_profile=get_object_or_404(Profile, pk = pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            new_profile.phone = form.cleaned_data['phone']
            new_profile.yog = form.cleaned_data['yog']
            new_profile.major = form.cleaned_data['major']
            new_profile.status = form.cleaned_data['status']
            new_profile.bio = form.cleaned_data['bio']
            new_profile.home = Home.objects.get(pk = form.cleaned_data['home'])
            new_profile.save()
            messages.success(request, 'You successfully updated your profile settings.')
            return HttpResponseRedirect(reverse(profile))
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = EditProfileForm(initial=model_to_dict(new_profile))

    return render(request, 'form.html', {'form': form})

@login_required
def edit_chore_deadline(request, pk):
    chore = get_object_or_404(Chore, pk = pk)
    if request.method == 'POST':
        form = EditChoreForm(request.POST)
        if form.is_valid():
            chore.deadline = form.cleaned_data['deadline']
            chore.save()

            return HttpResponseRedirect(reverse(reminders))
    else:
        proposed_deadline = datetime.date.today() + datetime.timedelta(weeks=1)
        form = EditChoreForm(initial={'deadline': proposed_deadline,})
    return render(request, 'chore_edit_form.html', {'form': form, 'chore': chore})

@login_required
def create_chore(request):
    if request.method == 'POST':
        form = CreateChoreForm(request.POST)
        if form.is_valid():
            chore = Chore.objects.create(title="", description="", created_on="2017-11-27", deadline="2017-12-04")
            chore.title = form.cleaned_data['title']
            chore.description = form.cleaned_data['description']
            chore.created_on = form.cleaned_data['created_on']
            chore.deadline = form.cleaned_data['deadline']

            chore.save()

            return HttpResponseRedirect(reverse(reminders))
    else:
        proposed_deadline = datetime.date.today() + datetime.timedelta(weeks=1)
        form = CreateChoreForm(initial={'deadline': proposed_deadline,})
    return render(request, 'chore_create_form.html', {'form': form})

@login_required
def delete_chore(request, pk):
    if request.method == 'POST':
        chore = get_object_or_404(Chore, pk = pk)
        chore.delete()

        return HttpResponseRedirect(reverse(reminders))
    return render(request, 'chore_delete_form.html', {})

def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                new_user = User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
                messages.success(request, 'You successfully created a new user. Sign in now.')
                return HttpResponseRedirect(reverse(profile))
            except IntegrityError as e:
                messages.error(request, "You have not met Django's built in attribute requirements. Try using a stronger password and a longer username.")
                return render(request, 'form.html', {'form': form})
        else:
            messages.error(request, 'Please correct the errors in the form.')
            return render(request, 'form.html', {'form': form})
    else:
        form = CreateUserForm()
    return render(request, 'form.html', {'form': form})

def edit_user(request, pk):
    updated_user = User.objects.filter(pk = pk)[0]
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            updated_user.username = form.cleaned_data['username']
            updated_user.email = form.cleaned_data['email']
            updated_user.set_password(form.cleaned_data['password'])
            updated_user.save()
            update_session_auth_hash(request, updated_user)
            messages.success(request, 'You successfully updated your account settings.')
            return HttpResponseRedirect(reverse(profile))
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = EditUserForm(initial = model_to_dict(updated_user))
    return render(request, 'form.html', {'form': form})

@login_required
def create_home(request):
    if request.method == 'POST':
        form = CreateHomeForm(request.POST)
        if form.is_valid():
            new_home = Home.objects.create(name = "", address = "", created_by = request.user.profile)
            new_home.name = form.cleaned_data['name']
            new_home.address = form.cleaned_data['address']
            new_home.leaseStart = form.cleaned_data['leaseStart']
            new_home.leaseEnds = form.cleaned_data['leaseEnds']
            new_home.save()
            request.user.profile.home = new_home
            request.user.profile.save()
            return HttpResponseRedirect(reverse(home))
    else:
        form = CreateHomeForm()
    return render(request, 'form.html', {'form': form})

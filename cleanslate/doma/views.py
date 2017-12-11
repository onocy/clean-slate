from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UserProfileForm, EditChoreForm, CreateChoreForm, CreateUserForm, CreateHomeForm
from .models import User, Profile, Home, Review, Forum, Post, Topic, Village, Transaction, Chore, Reminder, Event
from django.forms.models import model_to_dict
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
    user_groups = list(grouper(User.objects.all(), 4))

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
        bio = chosen_user.profile.bio
        email = chosen_user.profile.email
        return render(
            request,
            'profile.html',
                context = {
                'username' : chosen_user.username,
                'status' : status,
                'bio': bio,
                'email': email,
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
def EditUserProfileView(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    profile=get_object_or_404(Profile, pk = pk)

    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            profile.phone = form.cleaned_data['phone']
            profile.yog = form.cleaned_data['yog']
            profile.major = form.cleaned_data['major']
            profile.status = form.cleaned_data['status']
            profile.bio = form.cleaned_data['bio']
            profile.email = form.cleaned_data['email']
            profile.save()
            return HttpResponseRedirect('/doma/profile')
    else:
        form = UserProfileForm(initial=model_to_dict(profile))

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
            user = User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            return HttpResponseRedirect(reverse(profile))
    else:
        form = CreateUserForm()
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

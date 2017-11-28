from django.shortcuts import render

# Create your views here.
from .models import User, Home, Review, Forum, Post, Topic, Village, Transaction, Chore, Reminder, Event

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import EditChoreForm

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
    users = User.objects.all()

    # Render the HTML template home.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'num_topics': num_topics, 'users': users}
    )

def profile(request):
    """
    View function for individual profiles on site.
    """

    #Import profile information for specific profile based on ID?
    chosen_user = User.objects.get(id=1)

    first_name = chosen_user.first_name
    last_name = chosen_user.last_name
    full_name = first_name + ' ' + last_name
    status = chosen_user.status
    bio = chosen_user.bio
    return render(
        request,
        'profile.html',
        context={'full_name' : full_name
        , 'status' : status
        , 'bio': bio}
    )

    return render(
        request,
        'profile.html',
        context={}
    )


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
        context={'events': events, 'transactions':transactions, 'chores':chores}
    )


def finance(request):
    """
    View function for reminders (Later- not a separate page)
    """

    finance = Transaction.objects.all()



    return render(
        request,
        'finance_list.html',
        context={'transactions': finance}
    )

def edit_chore_deadline(request, pk):
    chore = get_object_or_404(Chore, pk = pk)
    if request.method == 'POST':
        form = EditChoreForm(request.POST)
        if form.is_valid():
            chore.deadline = form.cleaned_data['deadline']
            chore.save()
            return HttpResponseRedirect(reverse('reminders'))
    else:
        proposed_deadline = datetime.date.today() + datetime.timedelta(weeks=1)
        form = EditChoreForm(initial={'deadline': proposed_deadline,})
        return render(request, 'doma/chore_edit_form.html', {'form': form, 'chore': chore})

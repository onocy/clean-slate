from django.shortcuts import render

# Create your views here.

from .models import User, Home, Review, Forum, Post, Topic, Village, Transaction, Chore, Reminder, Event

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

from .forms import UserProfileForm
from django.shortcuts import get_object_or_404
from .models import Profile
from django.http import HttpResponse
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
            return HttpResponse('Hurray, saved!')
    else:
        form = UserProfileForm()

    return render(request, 'form.html', {'form': form})

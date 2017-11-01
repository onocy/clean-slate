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


    # Render the HTML template home.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'num_topics': num_topics}
    )

def profile(request):
    """
    View function for individual profiles on site.
    """

    #Import profile information for specific profile based on ID?


    return render(
        request,
        'profile.html',
        context={}
    )


def calendar(request):
    """
    View function for Calendar
    """

    return render(
        request,
        'calendar.html',
        context={}
    )


def reminders(request):
    """
    View function for reminders (Later- not a separate page)
    """

    return render(
        request,
        'reminders_list.html',
        context={}
    )


def finance(request):
    """
    View function for reminders (Later- not a separate page)
    """

    return render(
        request,
        'finance_list.html',
        context={}
    )
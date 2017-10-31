from django.shortcuts import render

# Create your views here.

from .models import User, Home, Review, Forum, Post, Topic, Village

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects

    num_users = User.objects.all().count()
    num_villages = Village.objects.all().count()
    num_posts = Post.objects.all().count()
    num_topics = Topic.objects.all().count()
    num_reviews = Review.objects.all().count()


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_users': num_users, 'num_villages': num_villages, 'num_posts': num_posts, 'num_topics': num_topics}
    )

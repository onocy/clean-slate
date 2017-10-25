from django.shortcuts import render

# Create your views here.

from .models import User, Home, Reviews, Forum, Post, Topic, Village

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_users=User.objects.all().count()
    num_villages=Village.objects.all().count()
    num_posts=Post.objects.all().count()
    num_topics=Topic.objects.all().count()
    num_reviews=Reviews.objects.all().count()
    
    # Available books (status = 'a')
#    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
#    num_authors=Author.objects.count()  # The 'all()' is implied by default.
#    num_genre = Genre.objects.count()
#    num_books_computer = Book.objects.filter(summary__icontains='computer').count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_users':num_users,'num_villages':num_villages,'num_posts':num_posts,'num_topics':num_topics}
    )

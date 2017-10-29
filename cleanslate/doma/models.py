from django.db import models
from django.urls import reverse


class User(models.Model):
    # reviews, forums, topics, and posts are one to many relations, so user will be foreign key in those models
    # make hidden
    password = models.CharField(max_length=100, help_text='Enter your password', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.TextField(max_length=1000, help_text='Enter a status for others to view')
    lastSeen = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, help_text='Enter your phone number', null=True, blank=True)
    bio = models.TextField(max_length=1000, help_text='Enter a brief description of yourself')
    yog = models.CharField(max_length=100, help_text='Enter your graduation date', null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=1)  # Select?
    home = models.OneToOneField('Home', on_delete=models.SET_NULL, null=True)
    smokes = models.BooleanField(default=False)
    bedtime = models.TimeField(null=True, blank=True)
    likesAnimals = models.NullBooleanField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)


class Home(models.Model):
    # I believe that user will be a foreign key in User, therefore, I have not set it here
    # createdBy = models.OneToOneField('User', on_delete=models.SET_NULL, null=True)
    # forum = models.OneToOneField('Forum', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, help_text='Enter your Home Name')
    address = models.CharField(max_length=100, help_text='Enter your Address', null=True)
    leaseStart = models.DateTimeField(null=True, blank=True)
    leaseEnds = models.DateTimeField()
    village = models.OneToOneField('Village', on_delete=models.SET_NULL, null=True, related_name='home_village')

    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return self.name



class Topic(models.Model):
    # posts = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True) (Check this, for relation from 1 to
    # many and many to 1)
    title = models.CharField(max_length=200, help_text="Enter a topic name")
    content = models.CharField(max_length=500)
    forum = models.ForeignKey('Forum', on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    created_on = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic-detail', args=[str(self.id)])


class Village(models.Model):
    home = models.ForeignKey('Home', on_delete=models.SET_NULL, null=True, related_name='village_home')
    forum = models.ForeignKey('Forum', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('village-detail', args=[str(self.id)])


class Review(models.Model):
    # Define fields
    # Define Methods
    '''
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    '''


class Forum(models.Model):
    # Define fields
    # Define Methods
    '''
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    '''


class Post(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a post name')
    content = models.CharField(max_length=500, help_text='Enter content')
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    posts = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    created_on = models.DateField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

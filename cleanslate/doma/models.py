from django.db import models
from django.urls import reverse


class User(models.Model):
    # reviews, forums, topics, and posts are one to many relations, so user will be foreign key in those models
    role_choices = (
        ('a', 'Admin'),
        ('u', 'User')
    )
    # make hidden
    password = models.CharField(max_length=100, help_text='Enter your password', null=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, help_text='Enter your phone number', null=True, blank=True)
    yog = models.CharField(max_length=100, help_text='Enter your graduation date', null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=1, choices=role_choices, default='u')

    status = models.TextField(max_length=1000, help_text='Enter a status for others to view')
    bio = models.TextField(max_length=1000, help_text='Enter a brief description of yourself')
    smokes = models.BooleanField(default=False, help_text='Do you smoke cigarettes?')
    bedtime = models.TimeField(null=True, blank=True, help_text='What is your usual sleep-time?')
    lastSeen = models.DateField(null=True, blank=True)
    email = models.EmailField(help_text='Enter your email')

    pet_allergies = models.NullBooleanField(null=True, blank=True, help_text='Are you allergic to pets?')
    home = models.OneToOneField('Home', on_delete=models.SET_NULL, null=True, related_name='user_home')

    def is_admin(self):
        return self.role in 'a'

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)


class Home(models.Model):
    createdBy = models.OneToOneField('User', on_delete=models.SET_NULL, null=True, related_name='home_creator')
    forum = models.OneToOneField('Forum', on_delete=models.CASCADE, null=False, primary_key=True)
    name = models.CharField(max_length=100, help_text='Enter your Home Name')
    address = models.CharField(max_length=100, help_text='Enter your Address', null=True)
    leaseStart = models.DateTimeField(null=True, blank=True)
    leaseEnds = models.DateTimeField()
    village = models.OneToOneField('Village', on_delete=models.SET_NULL, null=True, related_name='home_village')

    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return 'Home: %s' % self.name


class Topic(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a topic name")
    content = models.CharField(max_length=500)
    forum = models.ForeignKey('Forum', on_delete=models.CASCADE, null=False, primary_key=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    created_on = models.DateField()

    def __str__(self):
        return 'Topic: %s' % self.title

    def get_absolute_url(self):
        return reverse('topic-detail', args=[str(self.id)])


class Village(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a village name")
    home = models.ForeignKey('Home', on_delete=models.SET_NULL, null=True, related_name='village_home')
    forum = models.ForeignKey('Forum', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Village: %s' % self.title

    def get_absolute_url(self):
        return reverse('village-detail', args=[str(self.id)])


class Review(models.Model):
    reviewed = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='reviewed_user')
    reviewedBy = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='reviewer')

    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return '%s reviewed %s' % (self.reviewedBy, self.reviewed)


class Forum(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a forum name")
    description = models.TextField(max_length=1000, help_text='Enter a description for this forum')
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, null=False, primary_key=True)
    created_on = models.DateField()

    def get_absolute_url(self):
        return reverse('forum-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a post name')
    content = models.CharField(max_length=500, help_text='Enter content')
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, null=False, primary_key=True, related_name='op')
    created_on = models.DateTimeField()

    def __str__(self):
        return 'Post: %s' % self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Transaction(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a transaction name')
    description = models.CharField(max_length=500, help_text='Enter description')
    created_on = models.DateField()
    deadline = models.DateField(help_text='When is this transaction due?')
    amount = models.IntegerField()

    # debtors
    # creditors

    def __str__(self):
        return 'Transaction: %s' % self.title

    def get_absolute_url(self):
        return reverse('transaction-detail', args=[str(self.id)])


class Chore(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a chore name')
    description = models.CharField(max_length=500, help_text='Enter description')
    created_on = models.DateField()
    deadline = models.DateField(help_text='When is this chore due?')

    #owners

    def __str__(self):
        return 'Chore: %s' % self.title

    def get_absolute_url(self):
        return reverse('chore-detail', args=[str(self.id)])


class Reminder(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a reminder name')
    description = models.CharField(max_length=500, help_text='Enter description')
    created_on = models.DateField()
    deadline = models.DateField(help_text='When is this reminder due?')

    # owners

    def __str__(self):
        return 'Reminder: %s' % self.title

    def get_absolute_url(self):
        return reverse('reminder-detail', args=[str(self.id)])


class Event(models.Model):
    title = models.CharField(max_length=200, help_text='Enter an event name')
    description = models.CharField(max_length=500, help_text='Enter description')
    created_on = models.DateField()
    deadline = models.DateField(help_text='When is this event going to occur?')

    def __str__(self):
        return 'Event: %s' % self.title

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

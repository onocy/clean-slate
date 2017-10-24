from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.TextField(max_length=1000, help_text='Enter a status for others to view')
    lastSeen = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100)

    # make hidden 
    password = models.CharField(max_length=100, help_text='Enter your password')
    
    phone = models.CharField(max_length=10, help_text='Enter your phone number')
    bio = models.TextField(max_length=1000, help_text='Enter a brief description of yourself')
    # may not be necessary? 
    yog = models.CharField(max_length=100, help_text='Enter your graduation date')
    major = models.CharField(max_length=100)

    # fix select option
    homerole = models.CharField(max_length=1)

    # uncomment out home when Home model is declared
    home = models.OneToOneField('Home', on_delete=models.SET_NULL, null=True)

    # reviews, forums, topics, and posts are one to many relations, so user will be foreign key in those models
    smokes = models.BooleanField(default=False)
    bedtime = models.TimeField()
    likesAnimals = models.NullBooleanField()

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

class Home(models.Model):
    name = models.CharField(max_length=100)
    # I believe that user will be a foreign key in User, therefore, I have not set it here

    # createdBy = models.OneToOneField('User', on_delete=models.SET_NULL, null=True)
    leaseEnds = models.DateTimeField()
    # village = models.OneToOneField('Village', on_delete=models.SET_NULL, null=True)
    # forum = models.OneToOneField('Forum', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Reviews(models.Model):
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

class Topic(models.Model):
    # Define fields


    # Define Methods
    '''
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    '''

class Post(models.Model):
    # Define fields


    # Define Methods
    '''
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    '''

class Village(models.Model):
    # Define fields


    # Define Methods
    '''
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    '''

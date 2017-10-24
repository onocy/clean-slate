from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.TextField(max_length=1000, help_text='Enter a status for others to view')
    lastSeen = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100)
    # password
    # phone
    bio = models.TextField(max_length=1000, help_text='Enter a brief description of yourself')
    # class
    major = models.CharField(max_length=100)
    # homerole

    # uncomment out home when Home model is declared
    home = models.OneToOneField('Home', on_delete=models.SET_NULL, null=True)

    # reviews, forums, topics, and posts are one to many relations, so user will be foreign key in those models
    smokes = models.BooleanField(default=False)
    # bedtime
    # likesAnimals

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

class Home(models.Model):
    name = models.CharField(max_length=100)
    # I believe that user will be a foreign key in User, therefore, I have not set it here

    # createdBy = models.OneToOneField('User', on_delete=models.SET_NULL, null=True)
    leaseEnds = models.DateTimeField()
    village = models.OneToOneField('Village', on_delete=models.SET_NULL, null=True)
    # forum = models.OneToOneField('Forum', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a topic name")
    content = models.CharField(max_length=500)
    
    #posts = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True) (Check this, for relation from 1 to many and many to 1)
    forum = models.ForeignKey('Forum', on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    created_on = models.DateField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    
class Village(models.Model):
    home = models.ForeignKey('Home', on_delete=models.SET_NULL, null=True)
    forum = models.ForeignKey('Forum', on_delete=models.SET_NULL, null=True)
   
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

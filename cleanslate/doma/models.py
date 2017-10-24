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
    # home = models.OneToOneField('Home', on_delete=models.SET_NULL, null=True)

    # reviews, forums, topics, and posts are one to many relations, so user will be foreign key in those models
    smokes = models.BooleanField(default=False)
    # bedtime
    # likesAnimals

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

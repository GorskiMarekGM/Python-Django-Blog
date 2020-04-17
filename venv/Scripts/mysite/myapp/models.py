from django.db import models
# importing django utils for default
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# ORM - object relational mapper - allows to access database and use objects, 
# you can use different databases for one project

# Creating Post model
class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

# don t put timezone.now() because i don t want to execute this function 
# but just to store result in default variable
    date_posted = models.DateTimeField(default = timezone.now)

# foreign key to user in database
# on_delete - if user is deleted his posts also are deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

#special methods double underscored
    def __str__(self):
        return self.title

#create get absolute url method, so django will know how to find a location to specific post
# redirect - take you to page
# reverse - return url as string
    def get_absolute_url(self):
        #primary key of specyfic post
        return reverse('post-detail', kwargs={'pk':self.pk})

#       We need to make migrations after creating new model
#       Pillow Library for working with images in python

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    #model one to one relationship with User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #we want to be more specific then project.object, we need to tell how to print it out
    def __str__(self):
        return f'{self.user.username} Profile'

    #overriting save method
  #  def save(self, *args, **kwargs):
   #     super().save(*args, **kwargs)

        #resizing image
    #    img = Image.open(self.image.path)

     #   if img.height > 300 or img.width > 300:
      #      output_size = (300,300)
       #     img.thumbnail(output_size)
        #    img.save(self.image.path)




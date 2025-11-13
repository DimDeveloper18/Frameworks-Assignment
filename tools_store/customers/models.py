from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} User_profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        prof_img = Image.open(self.image.path)

        if prof_img.height > 70 or prof_img.width > 70:
            resize = (70, 70)
            prof_img.thumbnail(resize)
            prof_img.save(self.image.path)


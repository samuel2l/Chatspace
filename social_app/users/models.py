from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#we want users to have profile info but there is no way to append to the fields of the User model
#by default user model takres username,email,password. any other thing to add we need to create a new model
#sort of an extension for the user model. Hence it will be a one to one relationship
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dp=models.ImageField(default='default.jpg',upload_to='dps')

    def __str__(self):
        return f"{self.user.username}'s Profile"
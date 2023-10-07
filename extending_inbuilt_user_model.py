# You can extend Django's default User model by subclassing `AbstractUser`. This method allows you to create a custom User model while still 
# leveraging much of the built-in functionality provided by Django's `User` model. Here's how you can do it:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your custom fields here
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

# Abstract User has the full implementation of django's inbuilt user model i.e 
from django.contrib.auth.models import User

# Update the Settings to Use Your Custom User Model:
# In your project's settings (`settings.py`), specify your custom user model:

AUTH_USER_MODEL = 'customusers.CustomUser'

# And don't forget to makemigrations and run them

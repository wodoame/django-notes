# Set up your Django project:
# If you haven't already, create a Django project and app where you want to store the images.

# Define a model for your image:
# You'll need a model to represent the images you want to store in the database. 
# Create a new model or add a field to an existing model to store the image.

from django.db import models

class ImageModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default='default.jpg', upload_to='images/')
    # default just chooses a default image for example a profile picture by default when the user has not chose one yet.

# Configure your settings:
# Make sure you have configured your Django project to handle media files properly. 
# In your project's settings (settings.py), add the following settings:

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Also, make sure you have included the following in your project's urls.py to serve media files during development:

from django.conf import settings
from django.conf.urls.static import static

if setting.DEBUG: # that is if you are in development mode
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create and apply migrations:
# Run the following commands to create and apply migrations for your mode

python manage.py makemigrations
python manage.py migrate

# Notes
# <img src="{% image.url %} "> url is a method that returns the url of the current image object. It can be used in html to get the source


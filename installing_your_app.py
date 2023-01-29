# To install an app in Django, you will need to add it to the INSTALLED_APPS list
# in your project's settings file. This list tells Django which apps are available 
# for use in the project.

# First, navigate to the root directory of your project, and open the settings.py file.

# Then add the app name in the INSTALLED_APPS list like this:

INSTALLED_APPS = [
    # ...
    'your_app',
]

# after that you need to run the following command in the command prompt
# python manage.py makemigrations
# python manage.py migrate
# Finally, you can use the app in your project by importing it and 
# using its views, models, and other components.


# When installing an app in Django, you can also specify a custom AppConfig 
# class for the app. This is useful if you want to configure various settings 
# for the app, such as changing the default label name or adding custom behavior 
# when the app is ready.

# To install an app with a custom AppConfig class, you will first need to 
# create the AppConfig class in the app's apps.py file.

from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app'
    verbose_name = 'Your Custom App Name'

# Then, in the settings.py file, add the app to the INSTALLED_APPS list,
# specifying the path of the custom AppConfig class.

INSTALLED_APPS = [
    # ...
    'your_app.apps.YourAppConfig',
]


# Once you've added the custom AppConfig class to the INSTALLED_APPS list,
# you can use the app in your project by importing it and using its views, 
# models, and other components.

# After that, you need to run the following command in the command prompt


# python manage.py makemigrations
# python manage.py migrate

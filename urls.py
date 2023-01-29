# In Django, the urls.py file is used to define the URL patterns for the project.
# The basic structure of this file typically includes the following:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# This code imports the path function from the django.urls module and the views module from the current directory (.).
# The urlpatterns variable is a list of URL patterns that are matched against the requested URL.

# The path function is used to define the URL patterns. The first argument to the path function is the 
# URL pattern to match, and the second argument is the view function that should handle the request.

# The name parameter is used to give the URL pattern a unique name, which can be used to refer to it in other parts of the code.
# You can also use the include() function to include other URL patterns from other apps.

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app1/',include('app1.urls')),
    path('app2/',include('app2.urls')),
]

# This will include the urls from app1 and app2 in the project.
# This is useful when you want to split your url patterns across multiple apps in a project.
# In Django, you can pass parameters in the URL using the query string (the part after the question mark).
# In your `urls.py` file, you can define a URL pattern with a parameter like this:

from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example_view, name='example'),
]

# In your views.py, you can access the parameter using the `request.GET` dictionary:

from django.shortcuts import render

def example_view(request):
    your_parameter = request.GET.get('your_parameter')
    # Now 'your_parameter' contains the value passed in the URL

    # Your view logic here

    return render(request, 'your_template.html', context)

# Then, when you navigate to the URL `example/?your_parameter=value`, the `example_view` function will be called, 
# and you can access the value of `your_parameter` using `request.GET.get('your_parameter')`.
# Make sure to handle cases where the parameter might not be present or handle any validation as needed for your specific use case.

# You can use multiple parameters in the URL query string by separating them with an ampersand (`&`). Here's an example:

# In your `urls.py`:

from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example_view, name='example'),
]


# In your `views.py`:
from django.shortcuts import render

def example_view(request):
    param1 = request.GET.get('param1')
    param2 = request.GET.get('param2')

    # Your view logic here

    return render(request, 'your_template.html', context)

# Then, when you navigate to the URL `example/?param1=value1&param2=value2`, you can access both `param1` and `param2` in your `example_view` function.
# Remember to handle cases where parameters might not be present or handle any validation based on your requirements.

# The parameters in the query string don't affect the main URL because the query string is a way to pass additional information to the server or the application without changing the actual path of the URL.
# The main URL remains the same, and the query string is processed separately.

# For example, consider the URL: https://example.com/path/to/page?param1=value1&param2=value2

# In this URL:

# - The main URL is `https://example.com/path/to/page`.
# - The query string is `param1=value1&param2=value2`.

# The server or application uses the information in the query string for processing, but the main URL remains unchanged.
# This separation allows for passing dynamic parameters without altering the structure of the URL or the routing.
# If you need the URL to change dynamically based on parameters, you might want to explore using path parameters or other routing techniques.
# However, for many cases, especially in web applications, using query parameters is a common and convenient practice.

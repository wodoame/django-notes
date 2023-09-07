# Authentication is the process of verifying the identity of a user. 
# It involves confirming the user's credentials, such as a username and password, 
# to determine if the user is who they claim to be. 
# Once the user is authenticated, the application can grant access to specific resources
# or perform specific actions on behalf of the user.

# In Django, authentication is handled by the Django authentication system. The following are the steps to authenticate a user:

# 1. Import the authentication module:
from django.contrib.auth import authenticate, login

# 2. Check if the credentials provided by the user match any user in the database:
username = request.POST['username']
password = request.POST['password']
user = authenticate(request, username=username, password=password)

# 3. If the credentials match, the `authenticate()` function returns a User object, 
# otherwise it returns `None`. You can check if the user is authenticated as follows:
if user is not None:
 # User is authenticated, do something
else:
 # User is not authenticated, return an error message

# 4. To log the user in, use the `login()` function:
login(request, user)

# 5. Once a user is logged in, you can access the user's information using the `request.user` attribute. 
# You can check if the user is authenticated using `request.user.is_authenticated`.


# Django provides a built-in authentication system that includes views, forms, and other utilities for handling user authentication. 
# To set up authentication using the Django built-in login view, follow these steps:

# Define the authentication URLs in your project's urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ... other URL patterns ...

    # Login and Logout URLs
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
]
# the views we are importing are called class-based views
# the template_name paramter specifies a template where you would want to use for login or logout .
# Note that a form object is passed by the imported view to that template you choose. 
# so you can still do form.username, form.password ..etc 


# Specify the URL to redirect to after a successful login
LOGIN_REDIRECT_URL = 'index'  # Change this to your desired redirect URL

# the url is just the name of some specified route of your choice in the urlpatterns

# Specify the URL to redirect to after a successful logout
LOGOUT_REDIRECT_URL = 'login'  # Change this to your desired redirect URL


# Configure the authentication backend:
# Make sure that Django's authentication system is enabled by checking your settings.py file. The following line should be present:

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Secure your views (optional):
# If you want to restrict access to certain views to authenticated users, you can use the @login_required decorator in your views:

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def protected_view(request):
    # Your view logic here

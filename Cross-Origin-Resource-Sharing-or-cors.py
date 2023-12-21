# Configuring CORS (Cross-Origin Resource Sharing) headers in a Django application involves setting up the appropriate middleware to handle the HTTP headers that control cross-origin requests.
# Here's a step-by-step guide on how to configure CORS headers in a Django project:

# 1. **Install Django CORS Headers:**
#    Django CORS Headers is a third-party package that simplifies the process of handling CORS headers in Django. Install it using pip:
#    pip install django-cors-headers
   

# 2. **Update Django Settings:**
#    Open your Django project's settings file (`settings.py`) and add `'corsheaders'` to the `INSTALLED_APPS` and `MIDDLEWARE` lists:
   
   INSTALLED_APPS = [
       # ...
       'corsheaders',
       # ...
   ]

   MIDDLEWARE = [
       # ...
       'corsheaders.middleware.CorsMiddleware',
       # ... I read that it is recommended to put it at the beginning of the list
   ]
   

# 3. **Configure CORS Settings:**
#    Add the following CORS settings to your `settings.py`. Customize the `ALLOWED_ORIGINS` setting based on the origins from which you want to allow cross-origin requests.

   
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",  # Example: Your frontend app origin
       "https://yourfrontenddomain.com",
       "*", # for all origins
   ]

   # Optional: Allow credentials (cookies, authorization headers, etc.)
   CORS_ALLOW_CREDENTIALS = True

   # Optional: Customize allowed headers and methods
   CORS_ALLOW_HEADERS = [
       'access-control-allow-origin',
       'authorization',
       'content-type',
   ]
   
   CORS_ALLOW_METHODS = [
       'DELETE',
       'GET',
       'OPTIONS',
       'PATCH',
       'POST',
       'PUT',
   ]

 CORS_ALLOWED_ORIGIN_REGEXES = [
r"^https://\w+\.domain\.com$",
]
   

# Adjust the settings based on your specific needs. The `CORS_ALLOW_CREDENTIALS` setting allows or disallows sending credentials like cookies or HTTP authentication information with cross-origin requests.

# 4. **Update Django URLs (if needed):**
#    If you are serving APIs that need CORS support, ensure that the URLs are configured correctly. The `@api_view` decorator from Django REST Framework automatically adds CORS headers.

   
   from django.urls import path
   from rest_framework.decorators import api_view

   @api_view(['GET'])
   def my_api_view(request):
       # Your API view logic here
       return Response({'data': 'Hello, world!'})
   
   urlpatterns = [
       path('api/my-endpoint/', my_api_view),
       # Add other URL patterns as needed
   ]
   

# 5. **Test Your Configuration:**
# Restart your Django development server, and test your application by making cross-origin requests from your frontend application.

# For production, you might need to adjust settings based on your deployment environment and security requirements.
# Remember to consult the Django CORS Headers documentation for the latest information and additional configuration options: [django-cors-headers documentation](https://github.com/adamchainz/django-cors-headers).
# This is a useful blog I also found: https://www.stackhawk.com/blog/django-cors-guide/
# By following these steps, you should be able to configure CORS headers in your Django project and handle cross-origin requests appropriately.

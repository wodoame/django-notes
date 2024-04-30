# Accessing Cookies
In Django, the `request.COOKIES` object is a dictionary-like object that contains all the cookies sent by the client in the HTTP request. Each key in the dictionary represents the name of a cookie, and its corresponding value is the cookie's value.

Here's how you can use the `request.COOKIES` object in Django views:

```python
from django.http import HttpResponse

def my_view(request):
    # Accessing cookies sent by the client
    cookie_value = request.COOKIES.get('cookie_name')
    
    # Your view logic here
    # ...

    return HttpResponse(f"Cookie Value: {cookie_value}")
```

In this example:
- `request.COOKIES` is a dictionary-like object that contains all the cookies sent by the client.
- You can access a specific cookie value by using the `get()` method with the name of the cookie as the argument.
- If the cookie doesn't exist or if it's not sent with the request, `get()` will return `None`.

You can use the `request.COOKIES` object to retrieve any cookies sent by the client and use them in your views for various purposes, such as session management, authentication, or storing user preferences.

# Setting Cookies
In Django, setting cookies involves using the `HttpResponse.set_cookie()` method. This method allows you to add a cookie to the response object that will be sent to the client's browser.

Here's a basic example of how to set a cookie in Django:

```python
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('my_cookie_name', 'cookie_value')
    return response
```

In this example:

- We import the `HttpResponse` class from `django.http`.
- We define a view function `set_cookie` that takes a `request` object.
- Inside the view function, we create an `HttpResponse` object with the message "Cookie set!".
- We then call the `set_cookie()` method on the `HttpResponse` object to set a cookie named `'my_cookie_name'` with the value `'cookie_value'`.

You can also specify additional parameters for the cookie such as its expiration time, domain, path, and whether it should be secure or not. Here's an example of setting additional parameters:

```python
def set_cookie_with_params(request):
    response = HttpResponse("Cookie set with params!")
    response.set_cookie('my_cookie_name', 'cookie_value', max_age=3600, secure=True)
    return response
```

In this example, the `max_age` parameter sets the expiration time of the cookie to 3600 seconds (1 hour), and the `secure` parameter ensures that the cookie is only sent over HTTPS connections.

Remember, cookies are inherently insecure as they can be manipulated by the client. Be cautious about what data you store in cookies, especially sensitive information.

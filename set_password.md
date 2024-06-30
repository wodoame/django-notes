In Django, you can set a user's password programmatically using the `set_password()` method. Here's how you can do it:

```python
from django.contrib.auth.models import User

# Retrieve the user (replace 'john' with the actual username)
user = User.objects.get(username='john')

# Set the new password
user.set_password('new password')

# Save the user object
user.save()
```

This method ensures that the password is securely hashed and stored according to Django's password management system. If you're building custom forms for password setting or handling API calls to set passwords, this approach is quite handy.

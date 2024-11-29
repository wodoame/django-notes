Yes, you can have multiple settings files in a Django project, which is a common practice for separating environment-specific configurations (e.g., development, staging, production). Here’s how you can set it up:

---

### Steps to Use Multiple Settings Files in Django:

#### 1. **Organize Your Settings Files:**
Create a `settings` package (a directory with an `__init__.py` file) inside your project directory:

```
my_project/
├── my_project/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
```

- **`base.py`:** Contains settings common to all environments.
- **`development.py`:** Contains settings specific to the development environment.
- **`production.py`:** Contains settings specific to the production environment.

#### 2. **Configure `base.py`:**
Add all shared settings in `base.py`. Example:

```python
# base.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # other apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # other middleware
]

ROOT_URLCONF = 'my_project.urls'
WSGI_APPLICATION = 'my_project.wsgi.application'
```

#### 3. **Extend in `development.py` and `production.py`:**

```python
# development.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

```python
# production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'yourdbhost',
        'PORT': 'yourdbport',
    }
}
```

#### 4. **Set the Environment Variable:**

Django uses the `DJANGO_SETTINGS_MODULE` environment variable to determine which settings file to load. You can set it in your environment or manage it in a `.env` file.

- **For development:**

```bash
DJANGO_SETTINGS_MODULE=my_project.settings.development
```

- **For production:**

```bash
DJANGO_SETTINGS_MODULE=my_project.settings.production
```

#### 5. **Modify `manage.py` and `wsgi.py`:**

In both `manage.py` and `wsgi.py`, ensure `DJANGO_SETTINGS_MODULE` is referenced dynamically:

```python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings.development')
```

---

### Bonus: Automate Environment Switching

You can use a tool like **`django-environ`** to manage settings through a `.env` file:

1. Install it:
   ```bash
   pip install django-environ
   ```

2. Add it to `base.py`:
   ```python
   import environ

   env = environ.Env()
   environ.Env.read_env()  # reads a .env file

   SECRET_KEY = env('SECRET_KEY')
   DEBUG = env.bool('DEBUG', default=False)
   ```

3. Create a `.env` file:
   ```ini
   DJANGO_SETTINGS_MODULE=my_project.settings.development
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

Would you like help setting up any specific part of this structure?

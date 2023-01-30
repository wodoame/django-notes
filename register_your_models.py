# To register Django models in the admin interface, follow these steps:

# 1. Open the admin.py file in the app directory
# 2. Import the model you want to register
# 3. Create a class that inherits from admin.ModelAdmin
# 4. Register the model in the admin interface using the admin.site.register() method.

# Example:

from django.contrib import admin
# from .models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    # fields to display in the list view
    list_display = ('field1', 'field2')

# admin.site.register(YourModel, YourModelAdmin)


#```python
#from django.contrib import admin
#from .models import YourModel

#class YourModelAdmin(admin.ModelAdmin):
    # fields to display in the list view
#    list_display = ('field1', 'field2')

#admin.site.register(YourModel, YourModelAdmin)
#```

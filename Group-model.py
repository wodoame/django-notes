# In Django's `django.contrib.auth.models`, the **Group model** provides a generic way to categorize users.
# You can assign permissions or other labels to users by adding them to specific groups.
# Here are the key points about the `Group` model:

# 1. **Purpose**:
#    - The `Group` model allows you to organize users into logical groups.
#    - Users can belong to any number of groups.
#    - When a user is part of a group, they automatically inherit the permissions granted to that group.

# 2. **Fields**:
#    - `name`: A unique name for the group.
#    - You can create your own custom fields by extending the `Group` model.

# 3. **Usage**:
#    - To create a new group, you can define a model for it and add a `name` field (similar to how you create other models in Django)⁴.
#    - You can also extend the `Group` model by linking it to another model using a `OneToOneField`.

# Remember, the `Group` model is a powerful tool for managing permissions and organizing users within your Django application.

# When creating a **group** in Django, you'll need to follow these steps:

# 1. **Define a Model**:
#    - Create a new model for your group by extending the `Group` model provided by `django.contrib.auth.models`.
#    - Add any additional fields you need (e.g., description, permissions, etc.).

# 2. **Create Instances**:
#    - Instantiate the model to create actual group instances.
#    - Set the `name` field for each group.

# 3. **Assign Users**:
#    - Add users to the group using the `user.groups.add(group)` method.

# Here's a simple example:

# models.py
from django.contrib.auth.models import Group

class CustomGroup(Group):
    description = models.TextField()
# or you could just use the default Group model if you do not need to add more fields

# views.py or wherever you create groups
from .models import CustomGroup

# Create a new group
my_group = CustomGroup.objects.create(name='My Group', description='A custom group')

# Add users to the group
user1.groups.add(my_group)
user2.groups.add(my_group)


# In this example, we've extended the `Group` model to include a `description` field.
# Adjust the fields and logic according to your application's requirements. 

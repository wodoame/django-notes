# In Django, a OneToOneField is a field that is used to create a one-to-one relationship between two models.
# It's a type of relationship field that is commonly used when you want to create a strict one-to-one association between
# two different models, ensuring that each instance of one model is associated with exactly one instance of another model.

#   Here's how you define a OneToOneField in a Django model:
from django.db import models

class ModelA(models.Model):
    # Fields for ModelA

class ModelB(models.Model):
    related_model = models.OneToOneField(ModelA, on_delete=models.CASCADE)
    # Other fields for ModelB



# In the example above, we have two models: `ModelA` and `ModelB`. The `related_model` field in `ModelB` is a `OneToOneField` that creates a one-to-one
# relationship with `ModelA`. Here are a few key points to understand about `OneToOneField`:

# 1. **Uniqueness**: A `OneToOneField` enforces uniqueness, meaning that each instance of `ModelB` can be associated with only one instance of `ModelA`, and vice versa.
# This ensures that there is a one-to-one relationship between the two models.

# 2. **`on_delete` parameter**: The `on_delete` parameter specifies what should happen when the referenced object (`ModelA` in this case) is deleted.
# In the example, `models.CASCADE` is used, which means that when a `ModelA` instance is deleted, the associated `ModelB` instance will also be deleted.
# There are other options you can use for `on_delete`, like `models.PROTECT`, `models.SET_NULL`, and more.

# 3. **Reverse access**: When you create a `OneToOneField`, it creates a reverse relation in the referenced model.
# In this case, you can access the related `ModelB` instance from an instance of `ModelA` using the lowercase name of the related model (i.e., `modelb`).

# Here's how you can use a `OneToOneField` to create and access related objects:


# Creating related objects
model_a_instance = ModelA.objects.create()
model_b_instance = ModelB.objects.create(related_model=model_a_instance)

# Accessing related objects
related_b = model_a_instance.modelb  # Access the related ModelB instance
related_a = model_b_instance.related_model  # Access the related ModelA instance


# `OneToOneField` is useful when you have a specific use case where you want to ensure that each instance of one model corresponds to exactly one instance of another model.
# This can be useful in scenarios such as creating a user profile for each user, where each user has only one profile.

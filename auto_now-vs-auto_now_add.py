# In Django models, `auto_add` and `auto_now_add` are options used with `DateTimeField` to automatically set the field's value under certain conditions.
# Here's the difference between the two:

# 1. **`auto_now_add`:**
#    - When you set `auto_now_add=True` on a `DateTimeField`, it means that the field will be set to the current date and time when the object is created. Once set, the value of the field will not be updated.

   created_at = models.DateTimeField(auto_now_add=True)

   In this case, `created_at` will be set to the current date and time when the object is first saved to the database.

# 2. **`auto_now`:**
# When you set `auto_now=True` on a `DateTimeField`, it means that the field will be updated to the current date and time every time the object is saved, including both creation and subsequent updates.

last_updated_at = models.DateTimeField(auto_now=True)

# In this example, `last_updated_at` will be set to the current date and time when the object is created, and every time the object is updated and saved,
# the field will be automatically updated to the current date and time.

# This is often used to track the last modification time of an object in the database.
# Here's a summary of the two options:
# - `auto_now_add=True`: Sets the field to the current date and time only when the object is created and remains unchanged afterward.
# - `auto_now=True`: Updates the field to the current date and time every time the object is saved, including both creation and subsequent updates.

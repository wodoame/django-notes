# In Django, the `constraints` meta option allows you to define database constraints for your model.
# These constraints can enforce rules on your data, such as unique keys, foreign keys, and check constraints.
# Here's an example of how to use it:
# Suppose we have a `Book` model with a `title` field that should be unique within the database.
# We can define this constraint using the `constraints` meta option:


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_book_title')
        ]


# In this example:
# - The `unique=True` argument ensures that each book title is unique.
# - The `UniqueConstraint` specifies that the `title` field should have a unique constraint named `'unique_book_title'`.

# Apart from `UniqueConstraint`, there are other constraints you can use in Django models.
# Let me introduce a couple of them:

# 1. **CheckConstraint**:
#    - A `CheckConstraint` allows you to define custom conditions that must be satisfied for a record to be valid.
#    - For example, you can create a check constraint to ensure that the `end_date` is always greater than the `start_date` in an `Event` model:
     
     from django.db import models
     from django.db.models import CheckConstraint, Q, F

      class Event(models.Model):
          start_date = models.DateTimeField()
          end_date = models.DateTimeField()

          class Meta:
              constraints = [
                  CheckConstraint(
                      check=Q(end_date__gt=F('start_date')),
                      name='check_start_end_dates'
                  )
              ]
     
#    - In this example, the `check` argument specifies the condition, and the `name` argument provides a unique name for the constraint.

# 2. **Other Constraints**:
#    - There are additional constraints like `UniqueConstraint` and `CheckConstraint` that you can explore.

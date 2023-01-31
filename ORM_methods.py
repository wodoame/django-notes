# ORM (Object-Relational Mapping) in Django is a method to interact with databases using Python code instead of SQL. 
# Django provides several ORM methods to perform common database operations, including:
# 1. `all()`: Returns a QuerySet containing all the objects in the database table.
# 2. `filter(**kwargs)`: Returns a QuerySet containing objects that match the specified conditions.
# 3. `exclude(**kwargs)`: Returns a QuerySet containing objects that do not match the specified conditions.
# 4. `get(**kwargs)`: Returns a single object that matches the specified conditions. 
# If multiple objects match, a `MultipleObjectsReturned` exception is raised.
# 5. `create(**kwargs)`: Creates a new object and saves it to the database.
# 6. `update(**kwargs)`: Updates an existing object and saves it to the database.
# 7. `delete()`: Deletes an object from the database.
# These methods can be used on the model classes in your Django application to perform various database operations.


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.FloatField()

# Get all books
books = Book.objects.all()

# Filter books by author
books_by_author = Book.objects.filter(author='J.K. Rowling')

# Exclude books by author
books_not_by_author = Book.objects.exclude(author='J.K. Rowling')

# Get a single book by title
book = Book.objects.get(title='Harry Potter and the Philosopher\'s Stone')

# Create a new book and save to database
new_book = Book.objects.create(title='The Lord of the Rings', author='J.R.R. Tolkien', publication_date='1954-07-29', price=29.99)

# Update an existing book and save to database
book.title = 'The Lord of the Rings: The Fellowship of the Ring'
book.save()

# Delete a book from the database
book.delete()


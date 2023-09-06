# ME:
# What does relared_name do in Django models

# AI:
# In Django, the related_name attribute on a field is used to specify the name of the 
# reverse relationship from the related model back to the model that defines the field.

# ME:
# Show me some code explaining this

# AI:
# Sure, here is an example of how the related_name attribute is used in a Django model:

from django.db import models 
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

# so you would typically see code like this
author = Author.Objects.get(id=some_valid_id)
print(author.books.all()) # this is going to return a queryset of books associated with the author and the method .books is possible 
# because of the related_name parameter in the Book model. 
# Otherwise we would have done this. 
print(author.book_set.all()) # that is what is done by default the class name underscore set as the related_name.


# In this example, the Book model has a ForeignKey to the Author model.
# The related_name attribute is set to 'books', which means that when you have an instance
# of the Author model, you can use the 'books' attribute to access all the Book instances that have that author.

# ME:
# What about ManyToManyFields

# AI:
# You can also use related_name attribute with many to many fields as well.

class Person(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField("self", blank=True, related_name='known_by')

# In this example, the Person model has a ManyToManyField to itself.
# The related_name attribute is set to 'known_by', which means that when you
# have an instance of the Person model, you can use the 'known_by' attribute
# to access all the Person instances that know that person.

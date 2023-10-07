# In Django, the `on_delete` parameter is used when defining ForeignKey, OneToOneField, and other similar fields in a model to specify what should happen 
# when the referenced object (the object on the other side of the relation) is deleted.
# Here's how `on_delete` works and some of the common options:


# 1. **`CASCADE`**: When the referenced object is deleted, also delete the object that has the ForeignKey.
# This means that if you delete the referenced object, all objects that reference it will also be deleted.


class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.ForeignKey(Author, on_delete=models.CASCADE)

# 2. **`PROTECT`**: Prevent deletion of the referenced object by raising ProtectedError, a protected error will occur if you try to delete the 
# referenced object while it's still referenced by another object.

   
class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.ForeignKey(Author, on_delete=models.PROTECT)


# 3. **`SET_NULL`**: Set the ForeignKey field to `NULL` when the referenced object is deleted. This requires the field to be nullable.

class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)


# 4. **`SET_DEFAULT`**: Set the ForeignKey field to its default value when the referenced object is deleted.

class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)

# 5. **`SET()`**: Set the ForeignKey field to the value passed to `SET()` when the referenced object is deleted. 
# This allows you to specify a specific value to set the field to.

class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.ForeignKey(Author, on_delete=models.SET(1))


# 6. **`DO_NOTHING`**: Do nothing when the referenced object is deleted. You are responsible for handling the situation manually.

class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)


# It's important to choose the appropriate `on_delete` option based on your application's requirements.
# This ensures that your database maintains referential integrity and that data is handled correctly when related objects are deleted.

from django.db import models

# CharField: used for small-sized strings, usually for names, titles, etc.
# max_length: specifies the maximum length of the string. It's a required argument.
class Author(models.Model):
    name = models.CharField(max_length=100)

# IntegerField: used for positive or negative integers.
# default: sets a default value for the field.
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pages = models.IntegerField(default=0)

# FloatField: used for floating-point numbers.
# decimal_places: sets the number of decimal places to store with the float.
# max_digits: sets the maximum number of digits the float can have.
class Sales(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField(decimal_places=2, max_digits=5)
    units_sold = models.IntegerField()

# DateField: used for dates.
# auto_now: automatically sets the date to the current date every time the model is updated.
# auto_now_add: automatically sets the date to the current date when the model is first created.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.DateField(auto_now=False, auto_now_add=True)

# BooleanField: used for storing True/False values.
# default: sets a default value for the field.
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

 # TextField: used for large amounts of text, such as descriptions or content.
# blank: specifies if the field is allowed to be blank.
# null: specifies if the field is allowed to be null.
class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)

# EmailField: used for email addresses.
# max_length: specifies the maximum length of the string. It's a required argument.
class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

# URLField: used for URLs.
# max_length: specifies the maximum length of the string. It's a required argument.
class Website(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)

# ImageField: used for image files.
# upload_to: specifies the subdirectory within the `MEDIA_ROOT` to store the image.
class Cover(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='covers_images/')

# FileField: used for any file type.
# upload_to: specifies the subdirectory within the `MEDIA_ROOT` to store the file.
class Attachment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')

# TimeField: used for time of day.
# auto_now: automatically sets the time to the current time every time the model is updated.
# auto_now_add: automatically sets the time to the current time when the model is first created.
class Reading(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

# DateTimeField: used for dates and times.
# auto_now: automatically sets the date and time to the current date and time every time the model is updated.
# auto_now_add: automatically sets the date and time to the current date and time when the model is first created.
class Log(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True, auto_now_add=False)

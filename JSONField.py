# In Django, the `JSONField` is a field used to store JSON-encoded data.
# It's a flexible field that can store a variety of data structures, including lists and dictionaries, representing various Python data types.
# This allows you to store structured data in a single field in your model.
# In other words you can store actual python data types inside the field 

# Here's a simple example of using `JSONField` in a Django model:


from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    data = models.JSONField()


# In this example, the `data` field is a `JSONField` that can store JSON-encoded data.
# You can then store a variety of Python data types in this field, such as lists, dictionaries, strings, numbers, etc.


# Create and save an instance of MyModel
my_instance = MyModel(name='example', data={'key': 'value', 'numbers': [1, 2, 3]})
my_instance.save()

# Retrieve the data from the instance
retrieved_data = MyModel.objects.get(name='example').data
print(retrieved_data)
# Output: {'key': 'value', 'numbers': [1, 2, 3]}


# Keep in mind that while `JSONField` allows flexibility in storing various data types, it also means that you might lose some benefits of a relational database,
# such as indexing and querying on specific fields within the JSON data. 
# If you need to query or index specific fields within the JSON data, you might want to consider using a relational model with separate fields for each piece of data.
# Starting from Django 3.1, there is also a `JSONField` option `encoder` that allows you to specify a custom JSON encoder if needed. 
# This can be useful when you have custom data types that need to be serialized to JSON.

# When you retrieve a value from a `JSONField` in Django, the stored JSON data is automatically converted into the corresponding Python data types.
# Django's `JSONField` uses the `json` module in Python for serialization and deserialization.

# Here's an example to illustrate:
# Assume you have a Django model with a `JSONField`:

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    data = models.JSONField()


# Now, let's say you have an instance of `MyModel` with a JSON field:


# Create and save an instance
my_instance = MyModel(name='example', data={'numbers': [1, 2, 3], 'text': 'Hello'})
my_instance.save()


# When you retrieve the instance from the database and access the `data` field, Django automatically converts the stored JSON data into Python data types:

retrieved_instance = MyModel.objects.get(name='example')
retrieved_data = retrieved_instance.data

print(type(retrieved_data))
# Output: <class 'dict'>

print(retrieved_data['numbers'])
# Output: [1, 2, 3]

print(retrieved_data['text'])
# Output: 'Hello'


# In this example, `retrieved_data` is a Python dictionary, and you can access its values as you would with any Python dictionary.
# Django handles the conversion between the JSON representation stored in the database and the corresponding Python data types during the retrieval process.

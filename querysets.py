# Combining querysets (This does not handle uniqueness of elements)
queryset1 = Model.objects.filter(field1='value1')
queryset2 = Model.objects.filter(field2='value2')

# Use the '|' operator to create a new queryset that contains elements from both querysets
combined_queryset = queryset1 | queryset2

# In Django, you can make a queryset contain unique items after performing some combination by using the distinct() method.
# This method is often used with .values() or .values_list() to specify the fields by which you want to make the queryset's items unique. 
# Here's an example:

# Assuming you have a model called MyModel
from myapp.models import MyModel

# Create a queryset with some combination
queryset = MyModel.objects.filter(some_condition).values('field1', 'field2')

# Make the queryset contain unique items based on 'field1' and 'field2'
unique_queryset = queryset.distinct()

# Now unique_queryset will contain only unique items after the combination

# In this example, values('field1', 'field2') is used to select specific fields from the model, and then distinct() ensures that only unique 
# combinations of those fields are returned in the queryset.
# Remember to replace 'field1' and 'field2' with the actual field names you're interested in.

# creating an empty queryset
# You can create an empty queryset in Django by using the filter() method with a condition that is guaranteed not to match any records in the database.
# Here's one way to do it:
from myapp.models import MyModel

# Create an empty queryset by using a condition that is always False
empty_queryset = MyModel.objects.filter(pk__in=[])

# I found another way which is: 
empty_queryset = MyModel.objects.none() # This is the recommended way because .none() method was made for this purpose

# Now empty_queryset is an empty queryset
# In this example, we're using the filter() method with a condition that checks if the primary key (pk) is in an empty list. Since no primary key will ever be in an empty list, this queryset will always be empty.
# You can also create an empty queryset by chaining multiple filter conditions that can never be met, but the method above is a straightforward and clear way to create an empty queryset.

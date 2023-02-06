queryset1 = Model.objects.filter(field1='value1')
queryset2 = Model.objects.filter(field2='value2')

# Use the extend method to add queryset2 to the end of queryset1
queryset1.extend(queryset2)

#Note that extend modifies the queryset in place and returns None, it's similar to list.extend().

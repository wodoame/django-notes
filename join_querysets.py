queryset1 = Model.objects.filter(field1='value1')
queryset2 = Model.objects.filter(field2='value2')

# Use the '|' operator to create a new queryset that contains elements from both querysets
combined_queryset = queryset1 | queryset2
# Since a queryset is a set there are no duplicates.

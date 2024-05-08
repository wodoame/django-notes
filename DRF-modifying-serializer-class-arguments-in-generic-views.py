# Suppose you want to use a generic view but also you want some specific keyword arguments to be included when using the serializer class
# You can overrite the mixin methods for example .create() but for my case I wanted to preserve what it was already doing but include an extra keyword argument 'partial=True'
# I opened the method declaration (right click + Go to definition) in VsCode and just included the extra argument there

# Original code
 def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Modified version
 def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# other mixin methods can be overridden in the same way to achieve desired results  
# So you can use this if it becomes absolutely necessary.
# You must however try to find a better way first: For example if a field is not required everytime it's best to just 
# set it as not required in the models as opposed to using partial=True

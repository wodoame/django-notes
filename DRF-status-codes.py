# In Django Rest Framework (DRF), HTTP status codes are used to convey the result of API requests.
# DRF provides a set of status code constants that you can use when returning responses from your views or serializers.
# These constants are part of the `rest_framework` module. You can import them as follows:


from rest_framework import status


# Now, let's explore how these status codes can be used in DRF, particularly in views and serializers:

### In Views:
# In DRF views, you often return responses using the `Response` class. This class takes a status code as its first argument. Here's an example:


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyView(APIView):
    def get(self, request):
        # Some logic to retrieve data
        data = {'key': 'value'}

        # Returning a successful response with status code 200
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # Some logic to create a resource
        data = {'key': 'value'}

        # Returning a response indicating successful resource creation with status code 201
        return Response(data, status=status.HTTP_201_CREATED)

    def not_found(self, request):
        # Some logic to handle a case where a resource is not found
        return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)


# ### In Serializers:

# Serializers in DRF are responsible for converting complex data types, such as Django models, into native Python data types that can be easily rendered into JSON.
# When you encounter errors during the serialization process, you may need to raise an exception with an appropriate status code. Here's an example:


from rest_framework import serializers
from rest_framework import status

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

    def to_representation(self, instance):
        try:
            # Some custom logic that may raise an exception
            # ...

            # If everything is successful, return the serialized data
            return super().to_representation(instance)
        except SomeException as e:
            # If an exception occurs, raise it with a specific status code
            raise serializers.ValidationError({'error': str(e)}, status_code=status.HTTP_400_BAD_REQUEST)


# By using these constants from the `rest_framework` module, you can provide clear and standardized 
# information about the outcome of API requests in your Django Rest Framework application.

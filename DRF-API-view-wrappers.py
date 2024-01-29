# In Django Rest Framework (DRF), API view wrappers are classes or functions that provide a convenient way to organize and structure your views.
# They add functionality such as authentication, permissions, and response handling to your views.
# These wrappers help in writing clean and maintainable code for your API views.
# There are different types of view wrappers in DRF, and they include:

# 1. **`@api_view` Function Decorator:**
#    - The `@api_view` decorator is a function-level decorator that is used to define API views as function-based views.
#    It allows you to specify the HTTP methods that the view should respond to.

   
   from rest_framework.decorators import api_view
   from rest_framework.response import Response

   @api_view(['GET'])
   def example_view(request):
       content = {'message': 'Hello, World!'}
       return Response(content)
   

# 2. **`@APIView` Class-Based View:**
#    - The `APIView` class is a base class for class-based views in DRF.
#     It provides built-in methods for handling HTTP methods such as `get()`, `post()`, etc. By inheriting from `APIView`, you can easily structure your views and override methods as needed.

   
   from rest_framework.views import APIView
   from rest_framework.response import Response
   from rest_framework import status

   class ExampleView(APIView):
       def get(self, request):
           content = {'message': 'Hello, World!'}
           return Response(content, status=status.HTTP_200_OK)
   

# 3. **Generic Class-Based Views:**
#    - DRF provides a set of generic class-based views that are pre-built for common use cases. Examples include `ListAPIView`, `RetrieveAPIView`, `CreateAPIView`, etc.
#    These views are useful for handling standard CRUD operations.

   
   from rest_framework.generics import ListAPIView
   from .models import MyModel
   from .serializers import MyModelSerializer

   class MyModelListView(ListAPIView):
       queryset = MyModel.objects.all()
       serializer_class = MyModelSerializer
   

# 4. **Function-Based Views:**
#    - You can use regular Django function-based views with DRF by applying the `@api_view` decorator.
#    This allows you to use Django's `HttpRequest` and `HttpResponse` objects while still benefiting from DRF's additional features.

   
   from django.http import HttpResponse
   from rest_framework.decorators import api_view

   @api_view(['GET'])
   def my_function_view(request):
       return HttpResponse("Hello, World!")
   

# 5. **Mixins:**
#    - DRF includes mixins that provide reusable components for views. Mixins like `CreateModelMixin`, `UpdateModelMixin`, and `DestroyModelMixin` 
#    can be combined to create views that handle different aspects of model manipulation.

   
   from rest_framework.mixins import CreateModelMixin
   from rest_framework.viewsets import GenericViewSet

   class MyModelCreateView(CreateModelMixin, GenericViewSet):
       queryset = MyModel.objects.all()
       serializer_class = MyModelSerializer
   

# These view wrappers offer flexibility and modularity in organizing your API views.
# Depending on your requirements, you can choose the appropriate view wrapper to structure your views and leverage the features provided by DRF
# for authentication, permissions, serialization, and response handling.

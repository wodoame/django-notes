# Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django applications.
# When working with DRF, the `Request` and `Response` objects play a crucial role in handling incoming requests and crafting appropriate responses.
# NOTE: To make the Request and Response object work well you need to wrap your views with the api view wrappers. 
# Check the repository for api wrappers notes

### Request Object:
# The `Request` object in DRF represents the incoming HTTP request made by a client.
# It extends Django's `HttpRequest` and adds additional features and methods tailored for working with APIs.
# Some key aspects of the `Request` object include:

# 1. **Data Parsing:**
#    DRF's `Request` object automatically parses incoming data based on the request's content type.
#    For example, it can handle JSON, form data, or other content types seamlessly.

   
   data = request.data  # Access parsed request data
   

# 2. **Authentication:**
#    The `Request` object is responsible for managing authentication details.
#    DRF provides an easy way to retrieve the authenticated user associated with the request.

   
   user = request.user  # Access the authenticated user
   

# 3. **Query Parameters:**
#    The `Request` object provides easy access to query parameters.

   
   param_value = request.query_params.get('param_name')
   

# 4. **Request Methods:**
#    DRF's `Request` object allows you to easily check the HTTP method used for the request.

   
   if request.method == 'GET':
       # Handle GET request
   

### Response Object:
# The `Response` object in DRF is used to create HTTP responses returned to the client.
# It provides a simplified way to generate consistent and standardized responses.
# Key features of the `Response` object include:

# 1. **Status Codes:**
#    DRF's `Response` object allows you to set the HTTP status code for the response.

   
   return Response(data, status=status.HTTP_200_OK)
   

# 2. **Content Negotiation:**
#    Content negotiation is handled automatically by the `Response` object, allowing you to return data in multiple formats (e.g., JSON, XML).

   return Response(data, content_type='application/json')
   
# 3. **Pagination:**
#    DRF provides built-in support for pagination, making it easy to handle large result sets.

   return Response(data, status=status.HTTP_200_OK, headers=headers)
   
# 4. **Headers:**
#    You can set custom headers in the `Response` object.

   
   response = Response(data)
   response['X-Custom-Header'] = 'Custom Value'
   

# 5. **Response Rendering:**
#    DRF automatically renders the response content based on the accepted content types.

   return Response(data)

# In summary, the `Request` and `Response` objects in Django Rest Framework simplify the handling of incoming requests and the creation of consistent, formatted responses in API development. 
# They provide a convenient abstraction over Django's HttpRequest and HttpResponse, offering additional features tailored for building web APIs.

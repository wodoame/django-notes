In Django, `request.META` is a dictionary-like object that contains all available HTTP headers. It provides information about the request, the client's environment, and the server's configuration. Here are some common keys and methods that you can use with `request.META`:

1. **Accessing Specific Headers**:
   - `request.META['HTTP_HEADER_NAME']`: You can access specific HTTP headers by specifying their names in square brackets, preceded by 'HTTP_'. For example, to access the 'User-Agent' header, use `request.META['HTTP_USER_AGENT']`.

2. **HTTP Request Method**:
   - `request.META['REQUEST_METHOD']`: Retrieves the HTTP request method used, such as 'GET', 'POST', 'PUT', 'DELETE', etc.

3. **IP Address and Host**:
   - `request.META['REMOTE_ADDR']`: Gets the IP address of the client making the request.
   - `request.META['REMOTE_HOST']`: Retrieves the hostname of the client, if available.
   - `request.META['HTTP_HOST']`: Provides the host requested by the client in the HTTP 'Host' header.

4. **User-Agent**:
   - `request.META['HTTP_USER_AGENT']`: Contains the User-Agent string sent by the client's browser, which can be used to identify the client's browser and device.

5. **Content Type**:
   - `request.META['CONTENT_TYPE']`: Retrieves the content type of the request, such as 'application/json' or 'multipart/form-data'.

6. **Cookies**:
   - `request.META['HTTP_COOKIE']`: Contains the cookie data sent by the client in the 'Cookie' header.

7. **Referrer**:
   - `request.META['HTTP_REFERER']`: Provides the URL of the page that referred the client to the current page, if available.

8. **Server Information**:
   - `request.META['SERVER_NAME']`: Retrieves the server's hostname.
   - `request.META['SERVER_PORT']`: Gets the server's port (e.g., 80 for HTTP, 443 for HTTPS).

9. **Path Info and Script Name**:
   - `request.META['PATH_INFO']`: Contains the path part of the URL.
   - `request.META['SCRIPT_NAME']`: Provides the script name in the URL.

10. **Secure Connection**:
    - `request.META['HTTPS']`: Contains 'on' if the request was made over a secure (HTTPS) connection.

11. **HTTP Authentication**:
    - `request.META['HTTP_AUTHORIZATION']`: Contains the credentials for HTTP basic authentication, if provided by the client.

12. **Custom Headers**:
    - You can access custom headers sent by the client or added by your server by using `request.META['HTTP_CUSTOM_HEADER']`. Replace 'CUSTOM_HEADER' with the actual name of your custom header.

13. **Content Length**:
    - `request.META['CONTENT_LENGTH']`: Provides the length (in bytes) of the request content, if applicable.

Remember to use `request.META` with caution, as it contains sensitive information and user-provided data. Be mindful of security considerations, and always validate, sanitize, and properly handle data obtained from `request.META` to prevent security vulnerabilities.

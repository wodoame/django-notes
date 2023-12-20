# The `UploadedFile` object in Django provides several methods and attributes that allow you to interact with the uploaded file.
# Here are some commonly used ones:

### Attributes:
# - **name:** The original name of the uploaded file.
# - **size:** The size of the uploaded file in bytes.
# - **content_type:** The MIME type of the file, as provided by the browser.
# - **charset:** The character set of the file, if available.

### Methods:
# - **read([size]):** Reads and returns the specified number of bytes from the file. If no size is provided, it reads the entire file.
# - **readline([size]):** Reads and returns the next line from the file, up to the specified size.
# - **readlines([hint]):** Reads and returns a list of lines from the file. The optional hint argument specifies the approximate number of bytes to read.
# - **chunks([chunk_size]):** Yields chunks of the file data. This is useful for iterating over the file in chunks rather than reading the entire file into memory.
# - **seek(offset[, whence]):** Moves the file pointer to the specified offset. The whence parameter determines the reference point for the offset.
# - **multiple file processing methods:** There are several methods for handling multiple files submitted in a single request, such as `getlist()` and `getall()`. For example, `request.FILES.getlist('files')` would return a list of `UploadedFile` objects for all files uploaded with the name 'files'.

# Here's an example of using some of these methods:

uploaded_file = request.FILES.get('dataset')

# Accessing attributes
print(f"File Name: {uploaded_file.name}")
print(f"File Size: {uploaded_file.size} bytes")
print(f"Content Type: {uploaded_file.content_type}")

# Reading file content
content = uploaded_file.read(100)  # Read the first 100 bytes of the file

# Processing the file in chunks
for chunk in uploaded_file.chunks(chunk_size=1024):
    # Do something with each chunk of data
    pass

# Seeking to a specific position in the file
uploaded_file.seek(0)

# Reading lines from the file
lines = uploaded_file.readlines()

# These methods and attributes are handy when you need to process or inspect the contents of an uploaded file in Django.
# Depending on your use case, you can choose the methods that best suit your needs.

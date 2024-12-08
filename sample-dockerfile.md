```dockerfile
# Use an official Python image
FROM python:3.10-slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements file to leverage Docker's caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django app's code into the container
COPY . /app/

# Expose the port Django runs on (default: 8000)
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

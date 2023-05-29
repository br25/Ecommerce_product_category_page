# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port on which the Django application will run (change if necessary)
EXPOSE 8000

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:8000

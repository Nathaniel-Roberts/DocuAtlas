# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy everything from the local project directory to the /app directory in the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask to use 'app/main.py'
ENV FLASK_APP=app.main

# Expose port 5000 to allow access to the Flask app
EXPOSE 5000

# Define the command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

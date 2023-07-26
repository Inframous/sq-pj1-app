# Use an official Python runtime as a parent image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y wget gnupg2 unzip python3 python3-pip curl && \
    rm -rf /var/lib/apt/lists/*

# # Set up the working directory
WORKDIR /app

# Copy the app files into the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set up the environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV SQLALCHEMY_DATABASE_URI=sqlite:///users.db

# Expose port 80 for the Flask app to listen on
EXPOSE 80

# Set the environment variables for Flask
ENV FLASK_APP=app.py 
ENV FLASK_DEBUG=1

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

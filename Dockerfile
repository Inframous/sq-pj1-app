# Use an official Python runtime as a parent image
FROM ubuntu:22.04


# Install required packages
RUN apt-get update && \
    apt-get install -y wget gnupg2 unzip python3 python3-pip curl && \
    rm -rf /var/lib/apt/lists/*

# # Download and install Google Chrome
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#     echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
#     apt-get update && \
#     apt-get install -y google-chrome-stable=114.0.5735.106-1 && \
#     rm -rf /var/lib/apt/lists/*

# # Download and install ChromeDriver that matches the installed version of Chrome
# RUN CHROME_VERSION=$(google-chrome-stable --version | awk '{print $NF}' | sed 's/\..*//') && \
#     wget -q "https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION)/chromedriver_linux64.zip" && \
#     unzip chromedriver_linux64.zip && \
#     rm chromedriver_linux64.zip && \
#     mv chromedriver /usr/local/bin/
# # Set up the working directory
WORKDIR /app

# Copy the app files into the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set up the environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV SQLALCHEMY_DATABASE_URI=sqlite:///users.db

# Expose port 80 for the Flask app to listen on
EXPOSE 80

# Set the environment variables for Flask
ENV FLASK_APP=app.py 
ENV FLASK_DEBUG=1

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

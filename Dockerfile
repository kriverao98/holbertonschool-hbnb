# Dockerfile for hbnb project

# Use the Python 3.8 base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /usr/holbertonschool-hbnb

# Copy the entire project directory into the container
COPY . /usr/holbertonschool-hbnb/

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the port
ENV PORT=8000

# Expose the port to the outside world
EXPOSE 8000

# Create a volume for persistence
VOLUME ["/usr/holbertonschool-hbnb/Persistence"]

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]

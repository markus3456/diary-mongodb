# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY app.py /app/
COPY templates /app/templates/

# Install dependencies
RUN pip install Flask pymongo

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
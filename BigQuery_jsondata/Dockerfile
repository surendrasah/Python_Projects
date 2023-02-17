# Use a base image with Python
FROM python:3.9-slim

# Install the required libraries
RUN pip install requests google-cloud-bigquery

# Copy service account file into container
COPY bigquery_service_account_file.json /app/

# Set environment variable for service account file path
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/bigquery_service_account_file.json

# Copy the code into the container
COPY main.py /app/main.py

# Set the working directory to /app
WORKDIR /app

# Set the entry point to run the code
CMD ["python3", "main.py"]

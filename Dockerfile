# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./app ./app

# Expose port (default FastAPI port)
EXPOSE 8000

# Command to run the app using uvicorn
CMD ["/usr/local/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

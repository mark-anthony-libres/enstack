# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed, e.g., gcc for some packages)
# RUN apt-get update && apt-get install -y build-essential

# Copy only the requirements file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port uvicorn will run on (Cloud Run expects 8080 by default)
EXPOSE 8080

# Command to run your app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

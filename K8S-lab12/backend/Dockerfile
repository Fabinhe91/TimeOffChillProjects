# Use the Python image as base
FROM python:3.10-slim

# Install ca-certificates
RUN apt-get update && apt-get install -y ca-certificates

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt


# Copy the application code
COPY . .

# Expose the Flask API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

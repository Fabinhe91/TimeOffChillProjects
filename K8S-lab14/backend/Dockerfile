# Use a Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt /app/

# Install Python dependencies
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port for Flask
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]

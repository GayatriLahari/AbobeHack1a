# Base image with Python 3, limited size
FROM  python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your app code into the container
COPY app/ /app/

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your script
CMD ["python", "main.py"]
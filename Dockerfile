# Use Python 3.12 as the base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Run the application
CMD ["python", "main.py"]

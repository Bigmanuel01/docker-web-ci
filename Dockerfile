# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file first (to use Docker cache efficiently)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

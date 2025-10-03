# Use Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy all project files to container
COPY . .

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

# Base Python image
FROM python:3.9-slim

# Set the working directory (overridden per service in Compose)
WORKDIR /app

# Install dependencies dynamically for each service
ARG SERVICE_NAME
COPY ${SERVICE_NAME}/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy service-specific application code
COPY ${SERVICE_NAME}/app.py /app/

# Expose a default port
EXPOSE 5000

# Run the application dynamically
CMD ["python", "app.py"]

# Using an official python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dpeendencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (make sure its the one that FastAPI uses)
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
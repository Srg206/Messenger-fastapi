FROM python:3.9-alpine

# Copy requirements file
COPY requirements.txt .

# Install required packages
RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev openssl-dev

RUN pip install --upgrade pip


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

#RUN alembic upgrade d9026d92c241
# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


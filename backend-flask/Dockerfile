FROM ubuntu:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    mysql-client \
    libmysqlclient-dev

# Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Set the working directory
WORKDIR /code

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python3", "backend.py"]

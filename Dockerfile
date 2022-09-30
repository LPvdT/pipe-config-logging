# Base image
FROM python:3.10-slim-buster

# Install application Python package requirements
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Copy application source code
COPY . /app
WORKDIR /app

# Denote mount volumes
VOLUME [ "/app/logs", "/app/config", "app/dump" ]

# Entrypoint for direct deployment
ENTRYPOINT ["python", "entrypoint.py"]
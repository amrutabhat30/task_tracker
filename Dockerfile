# Use Python 3.12 as the base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /task_tracker
WORKDIR /task_tracker

# Copy the requirements.txt to the container and install dependencies
COPY requirements.txt ./
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove --purge -y build-essential python3-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire task_tracker project to the container
COPY . .

# Expose the port that the uWSGI server will run on
EXPOSE 8000

# Set the work directory
WORKDIR /task_tracker/server/uwsgi

# Command to run the application with python3.12
CMD ["uwsgi", "--ini", "develop.ini"]

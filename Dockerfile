# Use the official Ubuntu 22.04 image
FROM ubuntu:22.04

# Install system dependencies and Python 3.12
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.12 python3.12-venv python3.12-dev python3-pip \
    gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip for Python 3.12
RUN python3.12 -m pip install --upgrade pip

# Create and set the working directory
WORKDIR /task_tracker

# Copy the requirements file into the container
COPY requirements.txt /task_tracker/

# Install Python dependencies with python3.12
RUN python3.12 -m pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . /task_tracker/

# Expose the port your app runs on (default Django port is 8000)
EXPOSE 8000

WORKDIR /home/ubuntu/task_tracker/server/uwsgi

# Command to run the application with python3.12
CMD ["uwsgi", "--ini", "develop.ini"]

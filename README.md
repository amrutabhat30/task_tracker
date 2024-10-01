# Task Tracker Django Project

This project is a Django application for task management, using MySQL as the database. It includes a Docker setup for easy deployment and management.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [SQL Migration File](#sql-migration-file)
- [API Endpoints](#api-endpoints)


## Features
- Create, Read, Update, and Delete (CRUD) tasks.
- Paginated task retrieval.
- Built with Django REST Framework and documented with Swagger.

##

## Requirements
- Docker
- Docker Compose
- Python 3.12 or later

## Setup

### 1. Clone the Repositoryvggggggggg
```bash
git clone https://github.com/yourusername/task_tracker.git
cd task_tracker
```

### 2. Build the Docker Image
To build the Docker image, execute:
```bash
docker build -t task_tracker .
```
### 3. Start the Docker Containers
Use Docker Compose to start the application and the database:
```bash
docker run -d -p 8000:8000 <container_id>
```
### 4. Access the Application
Once the containers are running, you can access the application at:
```bash
http://<docker_ip_address>:8000
```

### 5. And the Swagger documentation at:
```bash
http://<docker_ip_address>:8000/swagger/
```

### 6. Run the migrations
```bash
mysql -u username -p database_name < ./task_tracker/migrations/tasks/create_tasks_table.sql
```

### 7. API Endpoints
```bash
GET /tasks/: Retrieve a list of tasks.
GET /tasks/{id}/: Retrieve a specific task by ID.
POST /tasks/: Create a new task.
PUT /tasks/{id}/: Update an existing task by ID.
DELETE /tasks/{id}/: Delete a task by ID.
```

### 8. Screenshots



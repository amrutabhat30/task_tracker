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


## Requirements
- Docker
- Docker Compose
- Python 3.12 or later

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task_tracker.git
cd task_tracker
```

### 2. Set up MySQL database
Install and configure MySQL server and run the following command
```bash
mysql -u username -p password < ./migrations/tasks/create_tasks_table.sql
```

### 3. Update Database credentials in settings
```bash
cd ./server/settings/develop.py

SQL_DETAILS = {
    # 'SQL_USER' : os.environ.get("JWT_RESOURCE_ID"),
    'USER': <USER>,
    'PASSWORD': <PASSWORD>,
    'HOST' : <HOST>,
    'DB_NAME' : <DB_NAME>,
    'PORT': <PORT>,
}

### 3. Build the Docker Image
To build the Docker image, execute:
```bash
docker build -t task_tracker .
```
### 4. Start the Docker Containers
Use Docker Compose to start the application and the database:
```bash
docker run -d -p 8000:8000 <container_id>
```
### 5. Access the Application
Once the containers are running, you can access the application at:
```bash
http://<docker_ip_address>:8000
```

### 6. And the Swagger documentation at:
```bash
http://<docker_ip_address>:8000/swagger/
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
#### Updating Task with Success resposne
![update_task](https://private-user-images.githubusercontent.com/17699193/372582278-b2a01f77-7421-47a7-90d7-04d32a7b9f77.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc4MDU1MDAsIm5iZiI6MTcyNzgwNTIwMCwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIyNzgtYjJhMDFmNzctNzQyMS00N2E3LTkwZDctMDRkMzJhN2I5Zjc3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDAxVDE3NTMyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM5NDllZGUxZTYwZjY0NjVmYTI5ZWQwMGM1ZTQwMjkwMjQyNzFkMzY4MzQxNjIwZWFlNTAyNzgwNmUxZGFmMDkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.g66yO7BZV3irqsV2DhsFgk095D09MNLQrLNKsWE1p7s)

#### Deleting a task that does not exist
![delete_task](https://private-user-images.githubusercontent.com/17699193/372582291-5df79401-ac55-454c-9533-f21429dba80e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc4MDU1MDAsIm5iZiI6MTcyNzgwNTIwMCwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIyOTEtNWRmNzk0MDEtYWM1NS00NTRjLTk1MzMtZjIxNDI5ZGJhODBlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDAxVDE3NTMyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdjMjM2MDM0ZTQ1MGJlOWUxNWY5YTRjNzlkMDc2ZWJjMjg0MjA3NmVhOTk1Y2ZmZTk1YWRlZTkyNDcxOGRjYjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.w0m7yGyM5Y7LG2t3rL79o5JZGjdiTCKQA1Xt1yMDwgk)

#### Get all tasks
![get_tasks](https://private-user-images.githubusercontent.com/17699193/372582299-952a0e6d-ada0-4efa-8f93-b7f8798bdc43.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc4MDU1MDAsIm5iZiI6MTcyNzgwNTIwMCwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIyOTktOTUyYTBlNmQtYWRhMC00ZWZhLThmOTMtYjdmODc5OGJkYzQzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDAxVDE3NTMyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRkYzgxODdlMWE1N2I5MWViYzFjNjlkYzFjZGQ4ZWE5NDFhNWI4MmYyOTU3ZDFlNTcwZjhiMzY3NDQ0OThlNTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.juvoP9Zsscx1-Ttk8n20GsX8lJK1-XMhpdhdA45_6Hw)

#### Create task
![create_task](https://private-user-images.githubusercontent.com/17699193/372582305-998dc738-d1e1-4a6d-9e4e-526375eebd48.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc4MDU1MDAsIm5iZiI6MTcyNzgwNTIwMCwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIzMDUtOTk4ZGM3MzgtZDFlMS00YTZkLTllNGUtNTI2Mzc1ZWViZDQ4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDAxVDE3NTMyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQ0Y2JjYjViNDdjM2Q2Y2U1ZjViMGU5YTVlOWU5ZmJkMmQ1MWYyZDJlZWJmNTg5ODBiMGNlYjRlZjU2ODk2M2EmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.d89opfZVr9syr3uOK-0loUD5hmTcSTIJAIxM2O077pE)

#### Create task without required field title
![create_task_error](https://private-user-images.githubusercontent.com/17699193/372582312-4bdeeb35-a903-47ad-b22e-593da9184991.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc4MDU1MDAsIm5iZiI6MTcyNzgwNTIwMCwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIzMTItNGJkZWViMzUtYTkwMy00N2FkLWIyMmUtNTkzZGE5MTg0OTkxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDAxVDE3NTMyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNjYjFkNTYxNDdlYzRhNzBjMjFiNDMxZDE4ZGM4MDA1YjAyYTZlYzExYzVlZTc4YzQ2Y2ZjOGRiMzQ0YWM5NDcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.rH7zlKqmQS4B0_a3EabNluzlLePM_PMvuSrqPimb5Sg)

#### Get a task
![get_task](https://private-user-images.githubusercontent.com/17699193/372582308-d4317c00-b18b-4afc-b178-11495295a99f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc4MDU1MDAsIm5iZiI6MTcyNzgwNTIwMCwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIzMDgtZDQzMTdjMDAtYjE4Yi00YWZjLWIxNzgtMTE0OTUyOTVhOTlmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDAxVDE3NTMyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdhOGFjMTQ5YTc5MzJmMzgyZjM1MzZkYWQxY2RiMzg3YTQxZTdhYWJjNGMzOWEyZjk0ZTc3MTEwMTA5NDAyMjcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.T7cpiQcNBBre22MNNhkVNCdL5ib2k5qTvIc5dKKvCvo)
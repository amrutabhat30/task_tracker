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
- MySQL
- Python 3.12

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task_tracker.git
cd task_tracker
```

### 2. Set up and start the application
```bash
docker-compose up -d
```

### 3. Access the Application and Database
You can access the application at:
```bash
http://localhost:8000
```
MySQL Database
```
localhost:3306
```

### 4. And the Swagger documentation at:
```bash
http://localhost:8000/swagger/
```

### 5. API Endpoints
```bash
GET /tasks/: Retrieve a list of tasks.
GET /tasks/{id}/: Retrieve a specific task by ID.
POST /tasks/: Create a new task.
PUT /tasks/{id}/: Update an existing task by ID.
DELETE /tasks/{id}/: Delete a task by ID.
```

### 6. Screenshots

#### Create task
![create_task](https://private-user-images.githubusercontent.com/17699193/372582305-998dc738-d1e1-4a6d-9e4e-526375eebd48.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjg5OTA3MjksIm5iZiI6MTcyODk5MDQyOSwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIzMDUtOTk4ZGM3MzgtZDFlMS00YTZkLTllNGUtNTI2Mzc1ZWViZDQ4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDE1VDExMDcwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYxOTMwZGNkNWEwNjA3ZDNjNTYwMmNjZmIyMTM0NTk3M2ZlOWRlOTliM2YwOWE1N2Y2YmVlZTVjMGEyM2UyZDcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.FwdkJikr7UX4lPTa6qFjJ6KJkHP9v73QtsLrdjhcwFA)

#### Create task without required field title
![create_task_error](https://private-user-images.githubusercontent.com/17699193/372582312-4bdeeb35-a903-47ad-b22e-593da9184991.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjg5OTA3MjksIm5iZiI6MTcyODk5MDQyOSwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIzMTItNGJkZWViMzUtYTkwMy00N2FkLWIyMmUtNTkzZGE5MTg0OTkxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDE1VDExMDcwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU4YjIwYTQ1NDI1NjRkODkwZjBhNmQzMjgyNjM1ZDg5ZWZhYTgzMjNhNTk0MzhlNjhhYTJjMjQxY2JiNDRlOTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.HDbXuZgUAcn56AgFvnIDQqFd_8xr9u3foVbxyrUcKd4)

#### Get specific task
![get_task](https://private-user-images.githubusercontent.com/17699193/372582308-d4317c00-b18b-4afc-b178-11495295a99f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjg5OTA3MjksIm5iZiI6MTcyODk5MDQyOSwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIzMDgtZDQzMTdjMDAtYjE4Yi00YWZjLWIxNzgtMTE0OTUyOTVhOTlmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDE1VDExMDcwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTcxYmM4ZGM1M2E5Nzc2YzYxZDdiMTNiOTE1OWQ2NGEyYmY4Y2U3MGQ5ZjM1MTIwOGE0ODQyOWJkODQxNDM2MDEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.ouVlriyduUhjzTHKiEcz-9RkV507pImG0rfo3lzUVx8)

#### Get all tasks
![get_all_tasks](https://private-user-images.githubusercontent.com/17699193/372582299-952a0e6d-ada0-4efa-8f93-b7f8798bdc43.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjg5OTA3MjksIm5iZiI6MTcyODk5MDQyOSwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIyOTktOTUyYTBlNmQtYWRhMC00ZWZhLThmOTMtYjdmODc5OGJkYzQzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDE1VDExMDcwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJlNzQyMzA0ZDM0YzhkZGZlY2FjYTA0YjJlZjkzMWJiZDM3ZjMxODNjYmRjNDVlMmQxZjc2NjBjMTgxYzI3ZDEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.f4knsqA8s9Btq4c6r_sIIlvtuRNcCqI-yXIlsnOWsoM)

#### Updating Task with Success response
![update_task](https://private-user-images.githubusercontent.com/17699193/372582287-6a1a559f-9e13-4670-a7bb-8d627bc3ada1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjg5OTA3MjksIm5iZiI6MTcyODk5MDQyOSwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIyODctNmExYTU1OWYtOWUxMy00NjcwLWE3YmItOGQ2MjdiYzNhZGExLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDE1VDExMDcwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIyMDJiNTM4Y2U3NDE2MTVlNDBiMTQ3MTZjMzhhYThkM2I4YzJhYjM0MjczYmY1ODU4MzgyZDVjZjYyMGEyMmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.-Ej5BP-nz_8YNFxyGbODJwTvP1NqEMsVSWDktPIsW04)

#### Deleting a task that does not exist
![delete_task](https://private-user-images.githubusercontent.com/17699193/372582291-5df79401-ac55-454c-9533-f21429dba80e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjg5OTA3MjksIm5iZiI6MTcyODk5MDQyOSwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIyOTEtNWRmNzk0MDEtYWM1NS00NTRjLTk1MzMtZjIxNDI5ZGJhODBlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDE1VDExMDcwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE4MzE4OWRmYjc1ZmQwM2E4YThmNWI5NmZkMzRmMTJkM2RiNjk5Y2FlYTE4M2I2YWZmOWQwNmEwMDYwYWUwYjImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.WmhKlZPBPpz27zK365dv0jiVdnyyYEIFI_6vl__SyT8)







#### Get a task
![get_task](https://private-user-images.githubusercontent.com/17699193/372582308-d4317c00-b18b-4afc-b178-11495295a99f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc4MDU1MDAsIm5iZiI6MTcyNzgwNTIwMCwicGF0aCI6Ii8xNzY5OTE5My8zNzI1ODIzMDgtZDQzMTdjMDAtYjE4Yi00YWZjLWIxNzgtMTE0OTUyOTVhOTlmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDAxVDE3NTMyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdhOGFjMTQ5YTc5MzJmMzgyZjM1MzZkYWQxY2RiMzg3YTQxZTdhYWJjNGMzOWEyZjk0ZTc3MTEwMTA5NDAyMjcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.T7cpiQcNBBre22MNNhkVNCdL5ib2k5qTvIc5dKKvCvo)
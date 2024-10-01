-- Use the task_tracker database
CREATE DATABASE IF NOT EXISTS task_tracker;
USE task_tracker;

-- Create the tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,               -- Primary key with auto increment
    title VARCHAR(255) NOT NULL,                     -- Title field with varchar type
    description TEXT,                                -- Description field with text type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Created at field with default current timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Updated at field with auto-update on record change
    deleted TINYINT(1) DEFAULT 0                     -- Soft delete indicator (0: not deleted, 1: deleted)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

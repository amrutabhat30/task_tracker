"""
MySQL database credentials
"""
import os
from dotenv import load_dotenv
from .settings import BASE_DIR

env_path = BASE_DIR + '/.env'  # If your .env is in the config folder
load_dotenv(dotenv_path=env_path)

SQL_DETAILS = {
    # 'SQL_USER' : os.environ.get("JWT_RESOURCE_ID"),
    'DB_NAME': os.getenv('MYSQL_DATABASE'),
    'USER': os.getenv('MYSQL_USER'),
    'PASSWORD': os.getenv('MYSQL_PASSWORD'),
    'HOST': os.getenv('MYSQL_HOST', 'mysql-db'),
    'PORT': os.getenv('MYSQL_PORT', '3306'),

}


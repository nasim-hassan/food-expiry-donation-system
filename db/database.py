import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DATABASE_HOST'),  # Load from .env
            user=os.getenv('DATABASE_USER'),  # Load from .env
            password=os.getenv('DATABASE_PASSWORD'),  # Load from .env
            database=os.getenv('DATABASE_NAME')  # Load from .env
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

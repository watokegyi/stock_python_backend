import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

def get_db_connection():
    try:
        connection=psycopg2.connect(
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            port="5432"
        )
        print("Connected to PostgreSQL")
        return connection
    except psycopg2.Error as error:
        print("Error connecting to PostgreSQL:",error)
        return None
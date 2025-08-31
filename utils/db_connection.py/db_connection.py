import sqlite3

DB_NAME = "cricbuzz.db"  # Database file (will be created automatically)

def create_connection():
    try:
        connection = sqlite3.connect(DB_NAME, check_same_thread=False)
        return connection
    except Exception as e:
        print("Database connection failed:", e)
        return None

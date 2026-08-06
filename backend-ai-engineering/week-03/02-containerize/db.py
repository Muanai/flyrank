import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    """Returns a new connection to the database."""
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is not set")
    # We use dict_row factory to easily convert rows to dictionaries
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)

def init_db():
    """Initialize the database schema and seed data if empty."""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            # 1. Create table if not exists
            # Using SERIAL for auto-incrementing ID in PostgreSQL
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    done BOOLEAN NOT NULL DEFAULT FALSE
                )
            """)
            
            # 2. Check row count
            cursor.execute("SELECT COUNT(*) FROM tasks")
            count = cursor.fetchone()["count"]
            
            # 3. Seed exactly three example tasks only when the table is empty
            if count == 0:
                seed_data = [
                    ("Membangun fondasi", True),
                    ("Menaklukkan memori fana", False),
                    ("Membakar kode usang", False)
                ]
                cursor.executemany(
                    "INSERT INTO tasks (title, done) VALUES (%s, %s)",
                    seed_data
                )
            
        # Commit the transaction
        conn.commit()

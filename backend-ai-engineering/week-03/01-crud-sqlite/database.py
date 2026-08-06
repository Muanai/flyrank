import sqlite3
import os

DB_FILE = "tasks.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT,
            done BOOLEAN
        )
    """)
    
    # Check row count
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Insert 3 example tasks
        seed_data = [
            ("Membangun fondasi", True),
            ("Menaklukkan memori fana", False),
            ("Membakar kode usang", False)
        ]
        cursor.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", seed_data)
    
    conn.commit()
    conn.close()

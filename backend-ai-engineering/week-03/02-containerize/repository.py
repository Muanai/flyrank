from db import get_db_connection

def get_all_tasks():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, title, done FROM tasks ORDER BY id ASC")
            return cursor.fetchall()

def get_task_by_id(task_id: int):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, title, done FROM tasks WHERE id = %s", (task_id,))
            return cursor.fetchone()

def create_task(title: str, done: bool = False):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING id, title, done",
                (title, done)
            )
            new_task = cursor.fetchone()
        conn.commit()
        return new_task

def update_task(task_id: int, title: str | None = None, done: bool | None = None):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            # Fetch current task state to merge updates
            cursor.execute("SELECT id, title, done FROM tasks WHERE id = %s", (task_id,))
            row = cursor.fetchone()
            if not row:
                return None
            
            new_title = title if title is not None else row["title"]
            new_done = done if done is not None else row["done"]
            
            cursor.execute(
                "UPDATE tasks SET title = %s, done = %s WHERE id = %s RETURNING id, title, done",
                (new_title, new_done, task_id)
            )
            updated_task = cursor.fetchone()
        conn.commit()
        return updated_task

def delete_task(task_id: int) -> bool:
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM tasks WHERE id = %s RETURNING id", (task_id,))
            deleted_row = cursor.fetchone()
        conn.commit()
        return deleted_row is not None

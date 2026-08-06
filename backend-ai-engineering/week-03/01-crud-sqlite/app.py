from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager
import sqlite3

from database import init_db, get_db_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Task API", version="1.0", lifespan=lifespan)

class TaskPayload(BaseModel):
    title: str | None = None

class UpdatePayload(BaseModel):
    title: str | None = None
    done: bool | None = None

@app.get("/", summary="Mendeskripsikan identitas API")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health", summary="Memeriksa denyut nadi peladen")
def health_check():
    return {"status": "ok"}

@app.get("/tasks", summary="Menampilkan seluruh daftar tugas")
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, done FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    
    return [{"id": row["id"], "title": row["title"], "done": bool(row["done"])} for row in rows]

@app.get("/tasks/{task_id}", summary="Mengambil satu tugas berdasarkan ID")
def get_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, done FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}
    
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.post("/tasks", status_code=201, summary="Menciptakan tugas baru")
def create_task(payload: TaskPayload):
    if not payload.title or not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title is missing or empty"})
    
    title = payload.title.strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, False))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return {"id": new_id, "title": title, "done": False}

@app.put("/tasks/{task_id}", summary="Mengubah wujud tugas yang ada")
def update_task(task_id: int, payload: UpdatePayload):
    if payload.title is not None and not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Invalid body"})
    if payload.title is None and payload.done is None:
        return JSONResponse(status_code=400, content={"error": "Empty body"})

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, title, done FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
        
    new_title = payload.title.strip() if payload.title is not None else row["title"]
    new_done = payload.done if payload.done is not None else bool(row["done"])
    
    cursor.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?", (new_title, new_done, task_id))
    conn.commit()
    conn.close()
    
    return {"id": task_id, "title": new_title, "done": new_done}

@app.delete("/tasks/{task_id}", status_code=204, summary="Menghancurkan tugas dari eksistensi")
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
        
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    
    return Response(status_code=204)

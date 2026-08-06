from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager

import repository
from db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database schema and seed data on startup
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
    tasks = repository.get_all_tasks()
    return tasks

@app.get("/tasks/{task_id}", summary="Mengambil satu tugas berdasarkan ID")
def get_task(task_id: int):
    task = repository.get_task_by_id(task_id)
    if task:
        return task
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.post("/tasks", status_code=201, summary="Menciptakan tugas baru")
def create_task(payload: TaskPayload):
    if not payload.title or not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title is missing or empty"})
    
    new_task = repository.create_task(title=payload.title.strip(), done=False)
    return new_task

@app.put("/tasks/{task_id}", summary="Mengubah wujud tugas yang ada")
def update_task(task_id: int, payload: UpdatePayload):
    if payload.title is not None and not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Invalid body"})
    if payload.title is None and payload.done is None:
        return JSONResponse(status_code=400, content={"error": "Empty body"})

    updated_task = repository.update_task(
        task_id=task_id,
        title=payload.title.strip() if payload.title else None,
        done=payload.done
    )
    
    if updated_task:
        return updated_task
            
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.delete("/tasks/{task_id}", status_code=204, summary="Menghancurkan tugas dari eksistensi")
def delete_task(task_id: int):
    deleted = repository.delete_task(task_id)
    if deleted:
        return Response(status_code=204)
            
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

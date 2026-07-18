from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Membangun fondasi", "done": True},
    {"id": 2, "title": "Menaklukkan memori fana", "done": False},
    {"id": 3, "title": "Membakar kode usang", "done": False}
]

class TaskPayload(BaseModel):
    title: str | None = None

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.post("/tasks", status_code=201)
def create_task(payload: TaskPayload):
    if not payload.title or not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title is missing or empty"})
    
    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": new_id, "title": payload.title.strip(), "done": False}
    tasks.append(new_task)
    return new_task
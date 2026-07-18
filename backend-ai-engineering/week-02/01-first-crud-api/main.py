from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Task API", version="1.0")

tasks = [
    {"id": 1, "title": "Membangun fondasi", "done": True},
    {"id": 2, "title": "Menaklukkan memori fana", "done": False},
    {"id": 3, "title": "Membakar kode usang", "done": False}
]

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
    return tasks

@app.get("/tasks/{task_id}", summary="Mengambil satu tugas berdasarkan ID")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.post("/tasks", status_code=201, summary="Menciptakan tugas baru")
def create_task(payload: TaskPayload):
    if not payload.title or not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title is missing or empty"})
    
    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": new_id, "title": payload.title.strip(), "done": False}
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", summary="Mengubah wujud tugas yang ada")
def update_task(task_id: int, payload: UpdatePayload):
    if payload.title is not None and not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Invalid body"})
    if payload.title is None and payload.done is None:
        return JSONResponse(status_code=400, content={"error": "Empty body"})

    for task in tasks:
        if task["id"] == task_id:
            if payload.title is not None:
                task["title"] = payload.title.strip()
            if payload.done is not None:
                task["done"] = payload.done
            return task
            
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.delete("/tasks/{task_id}", status_code=204, summary="Menghancurkan tugas dari eksistensi")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return Response(status_code=204)
            
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
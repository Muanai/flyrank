# Task API (First CRUD)

A minimalist RESTful API for managing a task list (To-Do List), built with FastAPI and running entirely on ephemeral memory. This project is an implementation of the FlyRank Internship Backend Track - W2 assignment.

## Installation & Running

This project rejects slow package managers and uses `uv` for absolute speed. 
Run this single command in your terminal to fire up the server on localhost:

```bash
uv run uvicorn main:app --reload
```
The server will start at http://localhost:8000.

## Endpoint List

| CRUD Operation | HTTP Method | Endpoint | Description |
|---|---|---|---|
| - | GET | / | API Identity |
| - | GET | /health | Server pulse check |
| Read | GET | /tasks | Display the entire task list |
| Read | GET | /tasks/{id} | Retrieve a single task by ID |
| Create | POST | /tasks | Create a new task |
| Update | PUT | /tasks/{id} | Alter the form of an existing task |
| Delete | DELETE | /tasks/{id} | Eradicate a task from existence |

## Usage Example (cURL)

```bash
$ curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
HTTP/1.1 201 Created
server: uvicorn
content-length: 43
content-type: application/json

{"id":4,"title":"Buy milk","done":false}
```

## Swagger UI
(Interactive documentation can be accessed at `/docs`)

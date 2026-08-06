# BE-04: Containerize Your Stack

This project is a migration of a FastAPI CRUD application to PostgreSQL, fully containerized using Docker and Docker Compose. It abstracts database logic into a Repository pattern.

## Project Overview

- **Database:** PostgreSQL running in a Docker container
- **Initialization:** The schema is automatically created and seeded on API startup via Python logic, eliminating the need for `init.sql`.
- **Infrastructure:** Managed via `docker-compose`, grouping `api` and `db` services.
- **Persistence:** Uses Docker volumes (`taskdata`) to retain PostgreSQL data between restarts.
- **Architecture:** Employs a single `repository.py` module to handle all SQL queries via `psycopg`, isolating data access from API routing logic.

## Setup Instructions

1. **Environment Setup:**
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. **Run the stack:**
   Use Docker Compose to build and start both the API and the Database:
   ```bash
   docker compose up --build
   ```
   *(Add `-d` to run in detached mode).*

## Endpoints

| Method | Endpoint      | Description |
|--------|---------------|-------------|
| GET    | `/tasks`      | Retrieve all tasks |
| GET    | `/tasks/{id}` | Retrieve a specific task by ID |
| POST   | `/tasks`      | Create a new task |
| PUT    | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example `curl` Output

```bash
$ curl http://127.0.0.1:8000/tasks
[
  {
    "id": 1,
    "title": "Membangun fondasi",
    "done": true
  },
  {
    "id": 2,
    "title": "Menaklukkan memori fana",
    "done": false
  },
  {
    "id": 3,
    "title": "Membakar kode usang",
    "done": false
  }
]
```

## Persistence Verification

To verify that data persists:
1. Create a task via a `POST /tasks` request.
2. Stop the containers: `docker compose down`
3. Start the containers again: `docker compose up`
4. The newly created task will still exist when checking `GET /tasks`.

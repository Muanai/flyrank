# BE-02: Connect CRUD API to SQLite

This project is a migration of a FastAPI CRUD application from in-memory storage to SQLite. The primary goal is to preserve the exact API contract while implementing database persistence.

## Features
- **Database:** SQLite (using standard library `sqlite3`)
- **Initialization:** Database file and table are automatically created on startup.
- **Seeding:** The database is seeded with 3 example tasks if it's empty.
- **API Contract:** Remains identical to the original in-memory version.
- **Persistence:** Data survives application restarts.

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   uvicorn app:app --reload
   ```

3. **Database:**
   The `tasks.db` file will be generated automatically when the application starts.

## Technical Notes
- Uses raw `sqlite3` without ORMs like SQLAlchemy.
- Includes parameterized queries for security.
- Educational focus on simple and correct separation of concerns.

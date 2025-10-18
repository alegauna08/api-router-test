# Copilot Instructions for trabajo-de-programacion

## Overview
This project is a FastAPI-based backend for managing songs (`Cancion`) with SQLite and PostgreSQL (Supabase) support. It includes endpoints for CRUD operations and file decompression utilities. The codebase is designed for educational and practical backend development.

## Major Components
- `trabajo.py`: Main FastAPI app using SQLite for local song management. Defines endpoints for listing, adding, modifying, and deleting songs. Uses Pydantic models and dependency injection for DB connections.
- `fastAPI+Supabase.py`: Example for connecting FastAPI to a PostgreSQL (Supabase) database using `psycopg`. Connection string must be configured for production use.
- `descomprimir.py`: Utility script for decompressing `.zip` and `.rar` files. Uses `zipfile` and `rarfile` (requires `pip install rarfile`).

## Developer Workflows
- **Run FastAPI app:**
  ```powershell
  uvicorn trabajo:app --reload
  ```
- **Install dependencies:**
  ```powershell
  pip install fastapi uvicorn pydantic rarfile psycopg
  ```
- **Test decompression:**
  ```powershell
  python descomprimir.py
  ```
- **Database migrations:**
  - SQLite tables are auto-created on app start via `crearTabla()`.
  - For PostgreSQL, table creation logic must be adapted (see commented code in `fastAPI+Supabase.py`).

## Project Conventions
- All API endpoints use dependency injection for DB connections.
- Pydantic models are used for request validation.
- Error messages are returned as JSON objects with `msg` keys.
- All decompression output is placed in the current working directory.
- Sensitive data (e.g., passwords) should be managed via environment variables, not hardcoded.

## Integration Points
- **Supabase/PostgreSQL:** Update the connection string in `fastAPI+Supabase.py` for production.
- **File decompression:** Ensure `rarfile` is installed for `.rar` support.

## Examples
- Add a song:
  ```json
  POST /agregar_cancion
  {
    "nombre": "Imagine",
    "compositor": "John Lennon",
    "genero": "Rock"
  }
  ```
- Decompress a file:
  ```powershell
  python descomprimir.py
  # Enter path to .zip or .rar when prompted
  ```

## Key Files
- `trabajo.py`: Main API logic
- `fastAPI+Supabase.py`: Supabase/PostgreSQL integration
- `descomprimir.py`: File decompression utility

---
If any workflow or integration is unclear, please provide feedback so instructions can be improved.

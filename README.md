# Fastback Project

Fastback is a modern web application built using FastAPI, designed to provide a robust and scalable backend for various use cases. The project is structured to follow best practices in API development and includes features such as database integration, CRUD operations, and API documentation.

## Features
- **FastAPI Framework**: Leverages the speed and simplicity of FastAPI for building APIs.
- **Database Integration**: Includes support for SQLite and async database operations using `aiosqlite` and `asyncpg`.
- **Pagination**: Implements pagination for API responses using `fastapi-pagination`.
- **MkDocs Documentation**: Comprehensive project documentation generated using MkDocs.

## Project Structure
```
app/
    __init__.py
    crud.py
    database.py
    main_config.py
    main.py
    models.py
    schemas.py

```

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fastback
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To start the application, run:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Documentation
To view the project documentation locally, start the MkDocs server:
```bash
mkdocs serve
```
Access the documentation at `http://127.0.0.1:9090`.


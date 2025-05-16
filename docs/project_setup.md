# Project Setup

## Prerequisites

- Docker and Docker Compose installed on your system.
- Python 3.10 or higher installed.
- A `.env` file with the necessary environment variables (e.g., `DATABASE_URL`, `HOST`, `PORT`).

## Steps to Set Up the Project

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastback
   ```

2. Build and start the Docker containers:
   ```
   docker-compose up --build
   ```

3. Access the application:
   - The FastAPI backend will be available at `http://<HOST>:<PORT>`.
   - The MkDocs documentation will be available at `http://localhost:9090`.

4. To stop the containers:
   ```
   docker-compose down
   ```

5. To run the application locally without Docker:
   ```
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --host <HOST> --port <PORT>
   ```
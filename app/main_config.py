from dotenv import load_dotenv
import os

load_dotenv()
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
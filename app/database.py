from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Aiven PostgreSQL connection URI (provided by Aiven)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://avnadmin:your_password@your-host.aivencloud.com:port/your_dbname?sslmode=require")

# SQLAlchemy async engine
engine = create_async_engine(DATABASE_URL, echo=False)

# Session factory
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for models
class Base(AsyncAttrs, DeclarativeBase):
    pass

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
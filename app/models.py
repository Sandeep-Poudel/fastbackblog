from .database import Base
from sqlalchemy import String,func
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

class Blog(Base):
    __tablename__ = "blogs"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[str] = mapped_column(String, server_default=func.now(), nullable=False)
    updated_at: Mapped[str] = mapped_column(String, server_default=func.now(), nullable=False, onupdate=func.now())
    pic: Mapped[str] = mapped_column(String, nullable=True)  # Allow NULL

# Pydantic models
class BlogCreate(BaseModel):
    title: str
    description: str
    author: str

class BlogUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    author: str | None = None

class BlogOut(BaseModel):
    id: int
    title: str
    description: str
    pic: str
    author: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

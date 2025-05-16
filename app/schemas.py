from pydantic import BaseModel
from typing import Optional

class BlogCreate(BaseModel):
    title: str
    description: str
    author: str

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None

class BlogOut(BaseModel):
    id: int
    title: str
    description: str
    author: str
    pic:str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
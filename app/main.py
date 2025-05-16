from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from .crud import get_all_blogs, create_blog, get_blog, update_blog, delete_blog
from .database import get_db, engine, Base
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from .models import BlogCreate, BlogUpdate, BlogOut
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

# Lifespan event to create tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="Blog API", version="1.0.0", lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CRUD Endpoints
@app.get("/blogs", response_model=List[BlogOut])
async def read_all_blogs(db = Depends(get_db)):
    return await get_all_blogs(db)

@app.post("/blogs", response_model=BlogOut, status_code=status.HTTP_201_CREATED)
async def create_new_blog(blog: BlogCreate, db = Depends(get_db)):
    db_blog = await create_blog(db, blog.title, blog.description, blog.author)
    if not db_blog:
        raise HTTPException(status_code=400, detail="Failed to create blog")
    return db_blog

@app.get("/blog/{blog_id}", response_model=BlogOut)
async def read_blog(blog_id: int, db = Depends(get_db)):
    blog = await get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@app.put("/blog/{blog_id}", response_model=BlogOut)
async def update_existing_blog(blog_id: int, blog_update: BlogUpdate, db = Depends(get_db)):
    blog = await update_blog(db, blog_id, **blog_update.dict(exclude_unset=True))
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@app.delete("/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_blog(blog_id: int, db = Depends(get_db)):
    blog = await get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    await delete_blog(db, blog_id)
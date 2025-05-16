from .models import Blog
from .database import AsyncSession
from sqlalchemy import select, update
import random

async def get_all_blogs(db: AsyncSession):
    result = await db.execute(select(Blog))
    return result.scalars().all()

async def create_blog(db: AsyncSession, title: str, description: str, author: str):
    db_blog = Blog(
        title=title, description=description, author=author,
        pic=f"https://picsum.photos/seed/{random.randint(1, 10000)}/600/400"
    )
    db.add(db_blog)
    await db.commit()
    await db.refresh(db_blog)
    return db_blog

async def get_blog(db: AsyncSession, blog_id: int):
    return await db.get(Blog, blog_id)

async def update_blog(db: AsyncSession, blog_id: int, title: str = None, description: str = None, author: str = None):
    blog = await db.get(Blog, blog_id)
    if not blog:
        return None
    update_data = {k: v for k, v in {"title": title, "description": description, "author": author}.items() if v is not None}
    if not update_data:
        return blog
    await db.execute(
        update(Blog).where(Blog.id == blog_id).values(**update_data)
    )
    await db.commit()
    await db.refresh(blog)
    return blog

async def delete_blog(db: AsyncSession, blog_id: int):
    blog = await db.get(Blog, blog_id)
    if blog:
        await db.delete(blog)
        await db.commit()
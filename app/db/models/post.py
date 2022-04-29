import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy import select, and_
from app.utils import generate_uuid4
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseOperation


class Post(BaseOperation):
    __tablename__ = "posts"
    id = Column(String, primary_key=True, default=generate_uuid4)
    author = Column(String, nullable=False)
    title = Column(String, nullable=False)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

    comments = relationship("Comment", lazy='joined', cascade="all, delete", back_populates="post")

    @classmethod
    async def create(cls, author: str, title: str, session, text: Optional[str]) -> str:
        post = cls(author=author, title=title, text=text)
        session.add(post)
        await session.commit()
        return post.id

    @classmethod
    async def get_by_author_and_title(cls, title: str, author: str, session: AsyncSession):
        stmt = select(cls).where(and_(cls.title == title, cls.author == author))
        result = await session.execute(stmt)
        return result.scalar()

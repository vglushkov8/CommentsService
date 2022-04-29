import datetime
from sqlalchemy import Column, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy import select, and_
from app.utils import generate_uuid4
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseOperation


class Comment(BaseOperation):
    __tablename__ = "comments"

    id = Column(String, primary_key=True, default=generate_uuid4)
    author = Column(String, nullable=False)
    text = Column(String, nullable=False)
    post_id = Column(String, ForeignKey('posts.id'))
    parent_comment_id = Column(String, ForeignKey('comments.id', ondelete='CASCADE'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

    post = relationship("Post", back_populates="comments")
    parent_comment = relationship("Comment", remote_side='Comment.id')

    @classmethod
    async def create(
        cls,
        author: str,
        text: str,
        post_id: str,
        session: AsyncSession,
        parent_comment_id: Optional[str] = None
    ) -> str:
        comment = cls(author=author, text=text, post_id=post_id, parent_comment_id=parent_comment_id)
        session.add(comment)
        await session.commit()
        return comment.id

from typing import Optional
from datetime import datetime
from .base import (
    BaseModel,
    BaseOrmModel,
)


class CommentModel(BaseOrmModel):
    id: str
    author: str
    text: str
    parent_comment_id: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]


class CreateCommentRequest(BaseModel):
    author: str
    text: str
    post_id: str
    parent_comment_id: Optional[str]


class GetCommentResponse(CommentModel):
    post_id: str


class UpdateCommentRequest(BaseModel):
    text: Optional[str]


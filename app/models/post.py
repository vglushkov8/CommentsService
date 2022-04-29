from typing import (
    Optional,
    List,
)
from .base import (
    BaseModel,
    BaseOrmModel,
)
from datetime import datetime
from .comment import CommentModel


class CreatePostRequest(BaseModel):
    author: str
    title: str
    text: Optional[str]


class GetPostResponse(BaseOrmModel):
    id: str
    author: str
    title: str
    text: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    comments: List[CommentModel]


class UpdatePostRequest(BaseModel):
    title: Optional[str]
    text: Optional[str]

from http import HTTPStatus
from fastapi import (
    APIRouter,
    HTTPException,
)
from app.db.config import async_session
from app.db.models.comment import Comment
from app.db.models.post import Post
from app.models.comment import (
    CreateCommentRequest,
    GetCommentResponse,
    UpdateCommentRequest,
)


router = APIRouter(
    prefix="/comment",
)


@router.post('/')
async def create_comment(request: CreateCommentRequest):
    async with async_session() as session:
        post = await Post.get_by_id(
            id_=request.post_id,
            session=session,
        )
        if not post:
            raise HTTPException(HTTPStatus.NOT_FOUND, f'post with id {request.post_id} not found')
        else:
            if request.parent_comment_id:
                parent_comment = await Comment.get_by_id(id_=request.parent_comment_id, session=session)
                if not parent_comment:
                    raise HTTPException(
                        HTTPStatus.NOT_FOUND, f'parent comment with id {request.parent_comment_id} not found'
                    )

            comment_id = await Comment.create(
                author=request.author,
                text=request.text,
                post_id=request.post_id,
                parent_comment_id=request.parent_comment_id,
                session=session
            )

            return {'id': comment_id}


@router.get('/{comment_id}')
async def get_comment(comment_id: str):
    async with async_session() as session:
        comment = await Comment.get_by_id(id_=comment_id, session=session)

    if comment:
        return GetCommentResponse.from_orm(comment)
    else:
        raise HTTPException(HTTPStatus.NOT_FOUND)


@router.put('/{comment_id}')
async def update_comment(comment_id: str, request: UpdateCommentRequest):
    async with async_session() as session:
        comment = await Comment.get_by_id(id_=comment_id, session=session)
        if not comment:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        await comment.update(
            session=session,
            text=request.text
        )


@router.delete('/{comment_id}')
async def delete_comment(comment_id: str):
    async with async_session() as session:
        comment = await Comment.get_by_id(id_=comment_id, session=session)
        if not comment:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        await Comment.delete(obj=comment, session=session)

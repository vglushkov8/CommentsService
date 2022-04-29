from http import HTTPStatus
from fastapi import (
    APIRouter,
    HTTPException,
)

from app.models.post import (
    CreatePostRequest,
    GetPostResponse,
    UpdatePostRequest,
)

from app.db.config import async_session
from app.db.models.post import Post


router = APIRouter(
    prefix="/post",
)


@router.post('/')
async def create_post(request: CreatePostRequest):
    async with async_session() as session:
        post = await Post.get_by_author_and_title(author=request.author, title=request.title, session=session)
        if not post:
            post_id = await Post.create(
                author=request.author,
                text=request.text,
                title=request.title,
                session=session
            )
        else:
            post_id = post.id

    return {'id': post_id}


@router.get('/{post_id}')
async def get_post(post_id: str):
    async with async_session() as session:
        post = await Post.get_by_id(id_=post_id, session=session)

        if post:
            return GetPostResponse.from_orm(post)
        else:
            raise HTTPException(HTTPStatus.NOT_FOUND)


@router.put('/{post_id}')
async def update_post(post_id: str, request: UpdatePostRequest):
    async with async_session() as session:
        post = await Post.get_by_id(id_=post_id, session=session)
        if not post:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        await post.update(
            session=session,
            title=request.title,
            text=request.text,
        )


@router.delete('/{post_id}')
async def delete_post(post_id: str):
    async with async_session() as session:
        post = await Post.get_by_id(id_=post_id, session=session)
        if not post:
            raise HTTPException(HTTPStatus.NOT_FOUND)

        await Post.delete(obj=post, session=session)

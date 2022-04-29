import uvicorn
from fastapi import FastAPI
from app.routes.comment import router as comments_router
from app.routes.post import router as posts_router
from app.settings import (
    SERVER_HOST,
    SERVER_PORT,
    LOG_CONFIG,
)

app = FastAPI()
app.include_router(posts_router)
app.include_router(comments_router)


if __name__ == '__main__':
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, log_config=LOG_CONFIG)

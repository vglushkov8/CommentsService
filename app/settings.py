import os
import uvicorn

SERVER_HOST = os.environ.get('SERVER_HOST', '127.0.0.1')
SERVER_PORT = os.environ.get('SERVER_PORT', 8080)
POSTGRES_USER = os.environ.get('POSTGRES_USER', "user")
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', "password")
POSTGRES_DB = os.environ.get('POSTGRES_DB', "db")
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', "localhost")
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

LOG_CONFIG = uvicorn.config.LOGGING_CONFIG
LOG_CONFIG["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
LOG_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

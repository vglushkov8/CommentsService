FROM python:3.8-slim

WORKDIR /root

COPY ./app ./app
COPY ./migrations ./migrations
COPY ./main.py .
COPY ./requirements.txt ./app/requirements.txt
COPY ./alembic.ini .

RUN pip install -r ./app/requirements.txt

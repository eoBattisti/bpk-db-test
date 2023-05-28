FROM python:3.8-slim

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COLUMN 80

RUN mkdir /setup
WORKDIR /setup/

RUN apt-get update

RUN apt-get -y install libpq-dev python3-dev gcc netcat make cron graphviz \
        postgresql postgresql-contrib musl-dev build-essential


COPY . /setup/

RUN sh ./docker/start.sh

ENTRYPOINT [ "./docker/entrypoint.sh" ]
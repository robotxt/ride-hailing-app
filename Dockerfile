FROM python:3.11-slim-bullseye AS base

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && apt-get install -y libpq-dev gdal-bin gcc
RUN apt-get install postgis -q -y --force-yes
RUN apt-get install postgresql-13-postgis-3
RUN pip install --upgrade pip poetry setuptools


# create user and make the app dir the working directory
RUN useradd -m -d /appuser/ appuser

FROM base AS django 

WORKDIR /server

# copy environment to the container
COPY wingz/. /server
COPY pyproject.toml poetry.lock /server/

# install python dependencies
RUN poetry cache clear --all pypi
RUN poetry config virtualenvs.create false && poetry update
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root
RUN poetry add python-dotenv

WORKDIR /server/

FROM python:3.9-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install -y --no-install-recommends gcc default-libmysqlclient-dev \
    && apt purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*
RUN pip install pipenv

ENV APP_NAME t_5_promo_core
ENV APP_HOME /$APP_NAME

WORKDIR $APP_HOME

ARG PIPENV_PIPFILE
ENV PIPENV_PIPFILE $PIPENV_PIPFILE

# it is need to copy PIPENV_PIPFILE too, sense $PIPENV_PIPFILE maybe different from default name Pipfile
COPY $PIPENV_PIPFILE .

COPY $PIPENV_PIPFILE.lock .
RUN PIPENV_PIPFILE=$PIPENV_PIPFILE PIPENV_VENV_IN_PROJECT=1 pipenv sync -d

COPY . .



FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install -y --no-install-recommends gcc default-libmysqlclient-dev gettext \
    && apt purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*
RUN pip install pipenv

ENV APP_NAME t_5_promo_core
ENV APP_HOME /$APP_NAME

WORKDIR $APP_HOME

COPY --from=builder $APP_HOME .

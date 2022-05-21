#  Dockerfile - django_gunicorn

###########
# BUILDER #
###########

# Base Python Image
FROM python:3.10-alpine as builder

# Set work directory
WORKDIR /usr/src/apps

# Python Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN apk update && apk add musl-dev gcc libffi-dev postgresql-dev python3-dev

# Install from requirements.txt
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/apps/wheels -r requirements.txt

#########
# FINAL #
#########

# Python base image
FROM python:3.10-alpine

# create directory for the apps user
RUN mkdir -p /home/apps

# Upgrade pip
RUN pip install --upgrade pip

# create the apps user
RUN addgroup -S apps && adduser -S apps -G apps

# create the appsropriate directories
ENV HOME=/home/apps
ENV apps_HOME=/home/apps/web
RUN mkdir $apps_HOME
RUN mkdir $apps_HOME/static
WORKDIR $apps_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/apps/wheels /wheels
COPY --from=builder /usr/src/apps/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $apps_HOME

# copy entrypoint.sh
COPY ./entrypoint.sh $apps_HOME

# chown all the files to the apps user
RUN chown -R apps:apps $apps_HOME

# chown for static volume
RUN mkdir /static
RUN chown apps:apps /static

# change to the apps user
USER apps

# run entrypoint.sh
ENTRYPOINT ["sh", "/home/apps/web/entrypoint.sh"]
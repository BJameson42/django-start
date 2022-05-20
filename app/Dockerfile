#  Dockerfile - django_gunicorn

###########
# BUILDER #
###########

# Base Python Image
FROM python:3.10-alpine as builder

# Set work directory
WORKDIR /usr/src/app

# Python Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN apk update && apk add musl-dev gcc libffi-dev postgresql-dev python3-dev

# Install from requirements.txt
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# Python base image
FROM python:3.10-alpine

# create directory for the app user
RUN mkdir -p /home/app

# Upgrade pip
RUN pip install --upgrade pip

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# chown for static volume
RUN mkdir /static
RUN chown app:app /static

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]
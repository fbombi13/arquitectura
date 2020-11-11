FROM python:3.8-slim-buster
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY  . .

# RUN python /code/manage.py makemigrations
# RUN python /code/manage.py migrate
# CMD python /code/manage.py runserver

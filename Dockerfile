FROM python:3.7.0-alpine3.8
RUN apk add --no-cache alpine-sdk bash git libffi-dev libxml2-dev libxslt-dev postgresql-dev
RUN pip install pipenv 
COPY . /srv/rsum
WORKDIR /srv/rsum
RUN pipenv install django
RUN pipenv run python manage.py makemigrations
RUN pipenv run python manage.py migrate 
RUN pipenv run python manage.py runserver 0.0.0.0:8000

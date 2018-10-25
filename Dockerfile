FROM python:3.7.0-alpine3.8
RUN apk add --no-cache git bash
RUN pip install pipenv 
COPY . /srv/rsum
WORKDIR /srv/rsum/rsum
RUN pipenv install
CMD python manage.py runserver

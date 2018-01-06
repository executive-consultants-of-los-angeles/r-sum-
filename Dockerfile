FROM python:alpine3.7
RUN apk update
RUN apk add postgresql-dev make g++
RUN pip install psycopg2 django

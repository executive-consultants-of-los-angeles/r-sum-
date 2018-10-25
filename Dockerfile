FROM python:3.7.0-alpine3.8
RUN apk add --no-cache alpine-sdk bash git libffi-dev libxml2-dev libxslt-dev openssl-dev
RUN pip install pipenv 
COPY . /srv/rsum
WORKDIR /srv/rsum/rsum

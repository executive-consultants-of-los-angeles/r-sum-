FROM python:rc-alpine
MAINTAINER duchess@gahan-corporation.com
RUN apk update
RUN apk add build-base git libxml2-dev libxslt-dev openldap-dev wget postgresql postgresql-dev
RUN mkdir -p /srv/rsum
WORKDIR /srv/rsum
RUN git clone https://github.com/gahan-corporation/rsum.application.git . 
RUN pip install -r .requirements
CMD rsum/manage.py runserver 0.0.0.0:8000

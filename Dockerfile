FROM python:alpine3.7
RUN apk update
RUN apk add git postgresql-dev make g++ libxml2-dev libxslt-dev bash
RUN pip install psycopg2 django git+https://github.com/executive-consultants-of-los-angeles/python-docx.git gunicorn pyyaml
ADD rsum /srv/rsum
ADD static /srv/static
CMD sh -c 'while sleep 3600; do :; done'

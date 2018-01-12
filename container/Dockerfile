FROM python:rc-alpine
RUN apk update
RUN apk add git wget postgresql postgresql-dev
RUN mkdir -p /srv/rsum
WORKDIR /srv/rsum
RUN git clone https://github.com/gahan-corporation/rsum.application.git . 
RUN pip install -r .requirements

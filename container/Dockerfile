FROM python:3.7-alpine
RUN apk update
RUN apk add git wget
RUN mkdir -p /srv/rsum
WORKDIR /srv/rsum
RUN git clone https://github.com/gahan-corporation/rsum.application.git . 
RUN pip install -r .requirements

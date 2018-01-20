FROM gcorp/rsum.application:build
MAINTAINER duchess@gahan-corporation.com
RUN apk add wget; wget https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 -O /usr/bin/cc-test-reporter; chmod +x /usr/bin/cc-test-reporter
RUN pip install codacy-coverage==1.3.10
WORKDIR /srv
ENV CC_TEST_REPORTER_ID 47df5e0000c73f07c1950f0da60b7e5bbc8b7021e646f20d0d8d2794c52d81b7
ENV PYTHONPATH /srv/rsum
RUN rm -r rsum
RUN git clone --branch tmp https://github.com/gahan-corporation/rsum.application.git rsum
WORKDIR /srv/rsum
RUN ln -sf /srv/rsum/static /srv/static
RUN pip install dj-database-url==0.4.2 
RUN pip install gunicorn==19.7.1
RUN pip install -r .requirements
RUN pip install git+https://github.com/gahan-corporation/rsum.application.git@v0.1.2
CMD gunicorn rsum.wsgi 

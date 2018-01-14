FROM gcorp/rsum.application:build 
MAINTAINER duchess@gahan-corporation.com
RUN apk add wget; wget https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 -O /usr/bin/cc-test-reporter; chmod +x /usr/bin/cc-test-reporter
RUN pip install codacy-coverage
WORKDIR /srv
RUN rm -r rsum 
RUN git clone https://github.com/gahan-corporation/rsum.application.git rsum
WORKDIR /srv/rsum
RUN ln -sf /srv/rsum/static /srv/static
RUN pip install -r .requirements
CMD rsum/manage.py runserver 0.0.0.0:8000

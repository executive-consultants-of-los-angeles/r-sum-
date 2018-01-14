FROM gcorp/rsum.application:build 
MAINTAINER duchess@gahan-corporation.com
WORKDIR /srv
RUN rm -r rsum 
RUN git clone https://github.com/gahan-corporation/rsum.application.git rsum
WORKDIR /srv/rsum
RUN ln -sf /srv/rsum/static /srv/static
RUN pip install -r .requirements
CMD rsum/manage.py runserver 0.0.0.0:8000

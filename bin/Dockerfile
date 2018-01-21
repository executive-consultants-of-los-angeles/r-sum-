FROM gcorp/rsum.application:build
MAINTAINER duchess@gahan-corporation.com
RUN pip install codacy-coverage==1.3.10
WORKDIR /srv
ENV PYTHONPATH /srv/rsum
ENV RSUM_ENV dev
RUN rm -r rsum
RUN git clone --branch iss173 https://github.com/gahan-corporation/rsum.application.git rsum
WORKDIR /srv/rsum
RUN ln -sf /srv/rsum/static /srv/static
RUN pip install dj-database-url==0.4.2 
RUN pip install gunicorn==19.7.1
RUN pip install -r .requirements
RUN pip install git+https://github.com/gahan-corporation/rsum.application.git@v0.1.2
COPY create bin/create
CMD gunicorn rsum.wsgi 

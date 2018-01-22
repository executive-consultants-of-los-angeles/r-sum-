FROM gcorp/rsum:build 
MAINTAINER duchess@gahan-corporation.com
WORKDIR /srv
ENV PYTHONPATH /srv/rsum
RUN rm -r /srv/rsum
ENV RSUM_ENV dev
RUN git clone --branch iss173 https://github.com/gahan-corporation/rsum.application.git rsum
WORKDIR /srv/rsum
RUN pip install git+https://github.com/gahan-corporation/rsum.application.git@v0.1.2
COPY create /bin/create
RUN apk add bash
CMD /bin/create 

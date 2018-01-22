FROM gcorp/rsum:build 
MAINTAINER duchess@gahan-corporation.com
WORKDIR /srv
ENV PYTHONPATH /srv/rsum
RUN rm -r /srv/rsum
ENV RSUM_ENV dev
RUN git clone --branch iss173 https://github.com/gahan-corporation/rsum.git
WORKDIR /srv/rsum
RUN pip install . 
COPY create /bin/create
RUN apk add bash
CMD /bin/create 

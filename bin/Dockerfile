FROM alpine:3.7 
MAINTAINER duchess@gahan-corporation.com
RUN apk update
RUN apk add python3
RUN apk add wget
RUN apk add git
RUN apk add postgresql
RUN apk add postgresql-dev
RUN ln -sf /usr/bin/python3 /usr/bin/python; wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py; rm get-pip.py; ln -sf /usr/bin/pip3 /usr/bin/pip;
WORKDIR /srv
ENV PYTHONPATH /srv/rsum
ENV RSUM_ENV dev
RUN git clone --branch iss173 https://github.com/gahan-corporation/rsum.application.git rsum
WORKDIR /srv/rsum
RUN pip install -r .requirements
RUN pip install git+https://github.com/gahan-corporation/rsum.application.git@v0.1.2
ADD create /bin/create
RUN apk add bash
CMD /bin/create 

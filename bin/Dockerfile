FROM gcorp/rsum:build 
MAINTAINER duchess@gahan-corporation.com
WORKDIR /srv
ENV PYTHONPATH /srv/rsum
ENV RSUM_ENV dev
RUN git clone --branch iss226 https://github.com/gahan-corporation/rsum.git
WORKDIR /srv/rsum
RUN pip uninstall -y rsum || true; pip uninstall -y rsum || true; python setup.py build; python setup.py install
COPY create /bin/create
RUN apk add bash
CMD /bin/create 

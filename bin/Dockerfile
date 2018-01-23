FROM gcorp/rsum:build 
MAINTAINER duchess@gahan-corporation.com
WORKDIR /srv
ENV PYTHONPATH /srv/rsum
ENV RSUM_ENV dev
ENV DJANGO_SETTINGS_MODULE=rsum.settings
RUN git clone https://github.com/gahan-corporation/rsum.git
WORKDIR /srv/rsum
RUN git fetch -p; git checkout v0.1.2; git checkout -b current
RUN pip uninstall -y rsum || true; pip uninstall -y rsum || true; python setup.py build; python setup.py install
COPY create /bin/create
RUN apk add bash
CMD /bin/create 

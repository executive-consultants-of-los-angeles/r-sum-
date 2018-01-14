FROM gcorp/rsum.application:build 
MAINTAINER duchess@gahan-corporation.com
RUN pip install -r .requirements
CMD rsum/manage.py runserver 0.0.0.0:8000

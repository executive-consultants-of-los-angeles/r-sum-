#!/bin/bash
docker rm -f apsql
docker rm -f arsum
docker rm -f angos
docker build -t apsql:latest /src/rsum/files/alex/apsql
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/apsql/r.yml
docker run -d --name apsql -p 5432:5432 -h apsql apsql /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/apsql/p.yml
docker build -t arsum:latest /src/rsum/files/alex/arsum
docker run -d --name arsum -p 8192:8192 -h arsum --link apsql arsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/arsum/p.yml
docker build -t angos:latest /src/rsum/files/alex/angos
docker run -d --name angos -p 3072:80 -h angos --link apsql --link arsum angos /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/angos/p.yml

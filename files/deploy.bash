#!/bin/bash

# Remove exiting containers.
docker rm -f apsql
docker rm -f arsum
docker rm -f angos
docker rm -f jrsum

# Remove existing images.
docker rmi -f apsql
docker rmi -f arsum
docker rmi -f angos
docker rmi -f jrsum

# apsql
docker build -t apsql:latest /src/rsum/files/alex/apsql
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/apsql/r.yml
docker run -d --name apsql -p 5432:5432 -h apsql apsql /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/apsql/p.yml

# arsum
docker build -t arsum:latest /src/rsum/files/alex/arsum
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/arsum/r.yml
docker run -d --name arsum -p 8192:8192 -h arsum --link apsql arsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/arsum/p.yml

# jrsum
docker build -t jrsum:latest /src/rsum/files/jess/jrsum
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/jess/jrsum/r.yml
docker run -d --name jrsum -p 8704:8704 -h jrsum --link apsql --link arsum -- link angos jrsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/jess/jrsum/p.yml

# angos
docker build -t angos:latest /src/rsum/files/alex/angos
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/angos/r.yml
docker run -d --link apsql --link arsum --name angos -p 3072:80 -h angos --link apsql --link arsum angos /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/angos/p.yml

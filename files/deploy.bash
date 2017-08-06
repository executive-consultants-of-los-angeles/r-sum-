#!/bin/bash
docker rm -f apsql
docker rm -f arsum
docker rm -f angos
docker build -t apsql:latest alex/apsql
docker run -d --name apsql -p 5432:5432 -h apsql apsql /usr/bin/supervisord -n
ansible-playbook alex/apsql/p.yml
docker build -t arsum:latest alex/arsum
docker run -d --name arsum -p 8192:8192 -h arsum --link apsql arsum /usr/bin/supervisord -n
ansible-playbook alex/arsum/p.yml
docker build -t angos:latest alex/angos
docker run -d --name angos -p 8192:8192 -h angos --link apsql --link arsum angos /usr/bin/supervisord -n
ansible-playbook alex/angos/p.yml

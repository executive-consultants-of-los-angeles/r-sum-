#!/bin/bash


# apsql
docker rmi -f apsql:archive
docker commit -m "Archive apsql for deploy." apsql apsql:archive
docker rm -f apsql
docker rmi -f apsql:latest
docker build -t apsql:latest /src/rsum/files/alex/apsql
/opt/py/bin/ansible-galaxy remove apsql 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/apsql/r.yml
docker run -d --name apsql -p 5432:5432 -h apsql apsql /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/apsql/p.yml

# angnx
docker rmi -f angnx:archive
docker commit -m "Archive angnx for deploy." angnx angnx:archive
docker rm -f angnx 
docker rmi -f angnx:latest
docker build -t angnx:latest /src/rsum/files/alex/angnx
/opt/py/bin/ansible-galaxy remove angnx 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/angnx/r.yml
docker run -d --name angnx -p 80:80 -p 443:443 -h angnx angnx /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/angnx/p.yml

# arsum
docker rmi -f arsum:archive
docker commit -m "Archive arsum for deploy." arsum arsum:archive
docker rm -f arsum
docker rmi -f arsum:latest
docker build -t arsum:latest /src/rsum/files/alex/arsum
/opt/py/bin/ansible-galaxy remove arsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/arsum/r.yml
docker run -d --name arsum -p 8192:8192 -h arsum --link apsql arsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/arsum/p.yml

# jrsum
docker rmi -f jrsum:archive
docker commit -m "Archive jrsum for deploy." jrsum jrsum:archive
docker rm -f jrsum
docker build -t jrsum:latest /src/rsum/files/jess/jrsum
/opt/py/bin/ansible-galaxy remove jrsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/jess/jrsum/r.yml
docker run -d --name jrsum -p 8704:8704 -h jrsum --link apsql --link arsum jrsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/jess/jrsum/p.yml

# angos
docker rmi -f angos:archive
docker commit -m "Archive angos for deploy." angos angos:archive
docker rm -f angos
docker rmi -f angos:latest
docker build -t angos:latest /src/rsum/files/alex/angos
/opt/py/bin/ansible-galaxy remove angos
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/angos/r.yml
docker run -d --link apsql --link arsum --name angos -p 3072:80 -h angos --link jrsum --link apsql --link arsum angos /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/angos/p.yml

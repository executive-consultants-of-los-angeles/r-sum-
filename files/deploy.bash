#!/bin/bash


export DD=`date +%Y%m%d-%H%M%s`

# apsql
docker commit -m "Archive apsql for deploy." apsql ecla/psql:$DD
docker push ecla/psql:$DD
docker rmi ecla/psql:$DD
docker rm -f apsql
docker rmi -f apsql:latest
docker build -t apsql:latest /src/rsum/files/alex/apsql
/opt/py/bin/ansible-galaxy remove apsql 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/apsql/r.yml
docker run -d --network arsum --name apsql -p 5432:5432 -h apsql apsql /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/apsql/p.yml

# arsum
docker commit -m "Archive arsum for deploy." arsum ecla/arsum:$DD
docker push ecla/arsum:$DD
docker rmi ecla/arsum:$DD
docker rm -f arsum
docker rmi -f arsum:latest
docker build -t arsum:latest /src/rsum/files/alex/arsum
/opt/py/bin/ansible-galaxy remove arsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/arsum/r.yml
docker run -d --network arsum --name arsum -p 8192:8192 -h arsum arsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/arsum/p.yml

# jrsum
docker commit -m "Archive jrsum for deploy." jrsum ecla/jrsum:$DD
docker push ecla/jrsum:$DD
docker rmi ecla/jrsum:$DD
docker rm -f jrsum
docker build -t jrsum:latest /src/rsum/files/jess/jrsum
/opt/py/bin/ansible-galaxy remove jrsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/jess/jrsum/r.yml
docker run -d --network arsum --name jrsum -p 8704:8704 -h jrsum jrsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/jess/jrsum/p.yml

# angos
docker commit -m "Archive angos for deploy." angos ecla/angos:$DD
docker push ecla/angos:$DD
docker rmi ecla/angos:$DD
docker rm -f angos
docker rmi -f angos:latest
docker build -t angos:latest /src/rsum/files/alex/angos
/opt/py/bin/ansible-galaxy remove angos
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/angos/r.yml
docker run -d --network arsum --name angos -p 3072:80 -h angos angos /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/angos/p.yml

# angnx
docker rmi -f angnx:archive
docker commit -m "Archive angnx for deploy." angnx angnx:archive
docker rm -f angnx 
docker rmi -f angnx:latest
docker build -t angnx:latest /src/rsum/files/alex/angnx
/opt/py/bin/ansible-galaxy remove angnx 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/alex/angnx/r.yml
docker run -d --network arsum --name angnx -p 80:80 -p 443:443 -h angnx angnx /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/alex/angnx/p.yml

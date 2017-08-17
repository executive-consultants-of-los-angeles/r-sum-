#!/bin/bash

export DD=`date +%Y%m%d-%H%M%s`

# arsum
docker commit -m "Archive arsum for deploy." arsum ecla/arsum:$DD
docker push ecla/arsum:$DD
docker rmi ecla/arsum:$DD
docker rm -f arsum
docker rmi -f arsum:latest
docker build -t arsum:latest /src/rsum/files/alex/arsum
/opt/py/bin/ansible-galaxy remove arsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/deploy/alex/requirements.yml
docker run -d --network arsum --name arsum -p 8192:8192 -h arsum arsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/deploy/alex/playbook.yml

# jrsum
docker commit -m "Archive jrsum for deploy." jrsum ecla/jrsum:$DD
docker push ecla/jrsum:$DD
docker rmi ecla/jrsum:$DD
docker rm -f jrsum
docker build -t jrsum:latest /src/rsum/files/jess/jrsum
/opt/py/bin/ansible-galaxy remove jrsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/jess/jrsum/requirements.yml
docker run -d --network arsum --name jrsum -p 8704:8704 -h jrsum jrsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/jess/jrsum/playbook.yml



#!/bin/bash

export DD=`date +%Y%m%d-%H%M%s`

# arsum
docker commit -m "Archive arsum for deploy." arsum ecla/arsum:$DD
docker push ecla/arsum:$DD
docker build -t arsum:latest /src/rsum/files/deploy/alex/
/opt/py/bin/ansible-galaxy remove arsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/deploy/alex/requirements.yml
# docker run -d --network arsum --name arsum -p 8192:8192 -h arsum arsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/deploy/alex/playbook.yml

# jrsum
docker commit -m "Archive jrsum for deploy." jrsum ecla/jrsum:$DD
docker push ecla/jrsum:$DD
docker build -t jrsum:latest /src/rsum/files/deploy/jess
/opt/py/bin/ansible-galaxy remove jrsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/deploy/jess/requirements.yml
# docker run -d --network arsum --name jrsum -p 8704:8704 -h jrsum jrsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/deploy/jess/playbook.yml

# tmrsum
docker build -t tmrsum:latest /src/rsum/files/deploy/alex-tm/
/opt/py/bin/ansible-galaxy remove tmrsum 
/opt/py/bin/ansible-galaxy install --force -r /src/rsum/files/deploy/alex/requirements.yml
# docker run -d --network arsum --name arsum -p 8192:8192 -h arsum arsum /usr/bin/supervisord -n
/opt/py/bin/ansible-playbook /src/rsum/files/deploy/alex/playbook.yml

# angnx
/opt/py/bin/ansible -m shell -a 'ansible-galaxy install -r /tmp/arsum.yml --force' angnx

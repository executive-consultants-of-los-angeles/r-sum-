FROM ecla/ansible:latest
ADD r.yml /tmp/r.yml
VOLUME /srv:/etc/ansible/roles/
RUN ansible-galaxy install -r /tmp/r.yml
ADD p.yml /tmp/p.yml
RUN ansible-playbook /tmp/p.yml

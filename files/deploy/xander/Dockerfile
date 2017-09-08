FROM ecla/ansible:latest
ADD requirements.yml /tmp/requirements.yml
RUN ansible-galaxy install -r /tmp/requirements.yml
ADD playbook.yml /tmp/playbook.yml

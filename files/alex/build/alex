FROM ecla/ansible:latest
ADD r_alex.yml /tmp/r.yml
RUN ansible-galaxy install -r /tmp/r.yml
ADD p_alex.yml /tmp/p.yml
RUN ansible-playbook /tmp/p.yml

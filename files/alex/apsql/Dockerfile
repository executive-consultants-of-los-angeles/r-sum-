FROM ecla/psql:latest
ADD r.yml /tmp/r.yml
RUN ansible-galaxy install -r /tmp/r.yml
ADD p.yml /tmp/p.yml

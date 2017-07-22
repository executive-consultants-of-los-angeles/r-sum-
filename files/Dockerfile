FROM ansible:latest 

RUN python get-pip.py
RUN apt-get -y install git
RUN rm get-pip.py
RUN pip install git+https://github.com/ansible/ansible.git 

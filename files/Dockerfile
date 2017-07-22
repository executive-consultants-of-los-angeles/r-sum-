FROM ansible:latest 

RUN apt-get -y install libapt-pkg-dev
RUN tar xvf python-apt_1.1.0~beta1build1.tar.xz
RUN cd python-apt-1.1.0~beta1; python setup.py build; python setup.py install 

FROM ansible:latest 

RUN pip install http://archive.ubuntu.com/ubuntu/pool/universe/p/python-distutils-extra/python-distutils-extra_2.39.orig.tar.gz
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/p/python-apt/python-apt_1.1.0~beta1build1.tar.xz
RUN tar xvf python-apt_1.1.0~beta1build1.tar.xz
RUN pip install python-apt_1.1.0-beta1build1

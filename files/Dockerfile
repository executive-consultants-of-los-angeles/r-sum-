FROM ansible:latest 

RUN git clone https://github.com/metacloud/molecule.git 
RUN cd molecule; python setup.py build; python setup.py install

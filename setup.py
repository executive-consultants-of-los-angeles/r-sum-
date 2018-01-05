"""Setup tools package information."""
import os
from setuptools import setup


def read(fname):
    """Load readme file.

    0. we have a top level README file and
    0.  it's easier to type in the README file than to put a raw

     string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rsum",
    version="0.0.1",
    author="Gahan Corporation",
    author_email="cfo@gahan-corporation.com",
    description=("rsum application"),
    license="The Unlicense",
    keywords="django",
    packages=[
        'rsum.home',
        'rsum.rsum'
    ],
    long_description=read('readme.rst'),
    setup_requires=['pytest-runner'],
    install_requires=['django', 'pyyaml'],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)

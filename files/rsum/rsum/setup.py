"""Setup tools package information."""
import os
from setuptools import setup


def read(fname):
    """Utility function to read the README file.  Used for the long_description.
    It's nice, because now

    0. we have a top level README file and
    0.  it's easier to type in the README file than to put a raw

     string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rsum",
    version="0.0.1",
    author="ECLA",
    author_email="cfo@ecla.solutiosn",
    description=("rsum application"),
    license="The Unlicense",
    keywords="accounting",
    packages=[
        'home',
        'rsum'
    ],
    long_description=read('readme.md'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'nose'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)

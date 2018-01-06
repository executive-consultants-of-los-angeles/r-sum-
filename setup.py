"""Setup tools package information."""
import os
from setuptools import setup


def read(fname):
    """Load readme file."""
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
        'rsum.rsum',
        'rsum.home',
        'rsum.home.models',
        'rsum.home.export',
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

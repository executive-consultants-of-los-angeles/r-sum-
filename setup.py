"""Setup tools package information."""
import os
from setuptools import setup


def read(fname):
    """Load readme file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rsum",
    version="0.1.2",
    author="Gahan Corporation",
    author_email="cfo@gahan-corporation.com",
    description=("rsum application"),
    license="The Unlicense",
    keywords="django",
    package_dir={'': 'rsum'},
    packages=[
        'rsum',
        'home',
        'home.models',
        'home.tests',
        'export',
        'export.tools',
        'export.sections',
        'export.tests'
    ],
    package_data={'': ['rsum/home/templates']},
    include_package_data=True,
    long_description=read('readme.md'),
    setup_requires=['pytest-runner'],
    install_requires=[
        'django', 'pyyaml',
        'django-extensions', 'django-s3-storage'
    ],
    tests_require=['pytest', 'coverage', 'pytest-django'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)

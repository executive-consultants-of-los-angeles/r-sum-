"""pytest configuration module."""
import pytest


class DB(object):
    """A DB object."""

    pass


@pytest.fixture(scope="session")
def db():
    """Return a DB object."""
    return DB()

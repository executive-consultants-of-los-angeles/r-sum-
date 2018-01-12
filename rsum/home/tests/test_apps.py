"""Module for testing apps."""


class TestApps(object):
    """Test home app."""

    assertion = True

    def test_home_app_name(self):
        """Test application name."""
        if not self.assertion:
            raise AssertionError()

"""Test module for profile class."""
import json


def test_profile_instance(profile):
    """Test profile save functionality."""
    test_profile = profile.create()

    if not isinstance(test_profile, profile):
        raise AssertionError()


def test_profile_attributes(profile):
    """Test for name and content fields in profile."""
    profile.create()
    profiles = profile.objects.all()

    for item in profiles:
        json_profile = json.loads(item.content)

        if not isinstance(item.name, str):
            raise AssertionError()

        if not isinstance(json_profile, (dict, list)):
            raise AssertionError()


def test_profile_create(profile, section):
    """Test the create method."""
    profile.create()
    sections = section.objects.all()

    for section_item in sections:
        if not isinstance(section_item.profile, profile):
            raise AssertionError()

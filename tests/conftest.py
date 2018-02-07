import pytest

from example_app import api as example_api


@pytest.fixture
def api():
    return example_api

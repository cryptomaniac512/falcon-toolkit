import pytest

import example_api


@pytest.fixture
def api():
    return example_api.api

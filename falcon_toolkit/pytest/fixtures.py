import falcon
import pytest

from .client import ApiTestClient


@pytest.fixture
def client(api: falcon.API):
    return ApiTestClient(api)

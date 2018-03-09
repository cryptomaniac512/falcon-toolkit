import falcon
import pytest

from .client import ApiTestClient


@pytest.fixture
def ApiTestClientCls():
    return ApiTestClient


@pytest.fixture
def client(api: falcon.API, ApiTestClientCls: ApiTestClient):
    return ApiTestClientCls(api)


@pytest.fixture
def default_client(api: falcon.API):
    return ApiTestClient(api)

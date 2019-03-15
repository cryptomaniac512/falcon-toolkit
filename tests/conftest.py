import pytest

import example_api
from pytest_falcon_client import ApiTestClient


@pytest.fixture
def api():
    return example_api.api


class CustomApiTestClient(ApiTestClient):
    def response_assertions(self, response):
        # test cors headers globally
        assert response.headers[
            'Access-Control-Allow-Origin'] == 'falconframework.org'

    def prepare_request(self, method, expected, *args, **kwargs):
        # add `ORIGIN` header to every request
        kwargs['headers'] = {'Origin': 'falconframework.org'}
        return args, kwargs


@pytest.fixture
def client(api):
    return CustomApiTestClient(api)

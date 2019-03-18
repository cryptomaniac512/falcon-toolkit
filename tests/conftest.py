import pytest

import example_api
from pytest_falcon_client import ApiTestClient


@pytest.fixture
def cors_api():
    return example_api.cors_api


@pytest.fixture
def api():
    return example_api.api


class CorsApiTestClient(ApiTestClient):
    def response_assertions(self, response):
        # test cors headers globally
        assert response.headers[
            'Access-Control-Allow-Origin'] == 'falconframework.org'

    def prepare_request(self, method, expected, *args, **kwargs):
        # add `ORIGIN` header to every request
        kwargs['headers'] = {'Origin': 'falconframework.org'}
        return args, kwargs, expected


@pytest.fixture
def cors_client(cors_api):
    return CorsApiTestClient(cors_api)


@pytest.fixture
def client(make_client, api):
    return make_client(api)

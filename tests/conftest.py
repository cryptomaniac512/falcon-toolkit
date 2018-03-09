import pytest

import example_api


@pytest.fixture
def api():
    return example_api.api


@pytest.fixture
def ApiTestClientCls(ApiTestClientCls):

    class ApiTestClient(ApiTestClientCls):

        def response_assertions(self, response):
            # test cors headers globally
            assert response.headers[
                'Access-Control-Allow-Origin'] == 'falconframework.org'

        def prepare_request(self, method, expected, *args, **kwargs):
            # add `ORIGIN` header to every request
            kwargs['headers'] = {'Origin': 'falconframework.org'}
            return args, kwargs

    return ApiTestClient

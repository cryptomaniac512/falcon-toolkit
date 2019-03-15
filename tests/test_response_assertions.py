import pytest

from pytest_falcon_client import ApiTestClient


class FailurableApiTestClient(ApiTestClient):
    def response_assertions(self, response):
        assert response.headers['Access-Control-Allow-Origin'] == '*'

    def prepare_request(self, method, expected, *args, **kwargs):
        # add `ORIGIN` header to every request
        kwargs['headers'] = {'Origin': 'falconframework.org'}
        return args, kwargs


@pytest.fixture
def fail_client(api):
    return FailurableApiTestClient(api)


def test_success(client):
    client.get('/example/20/')


def test_fails(fail_client):
    with pytest.raises(AssertionError):
        fail_client.get('/example/20/')

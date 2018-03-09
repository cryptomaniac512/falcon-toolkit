import pytest


@pytest.fixture
def fail_client(api, ApiTestClientCls):

    class ApiTestClient(ApiTestClientCls):
        def response_assertions(self, response):
            assert response.headers['Access-Control-Allow-Origin'] == '*'

    return ApiTestClient(api)


def test_success(client):
    client.get('/example/20/')


def test_fails(fail_client):
    with pytest.raises(AssertionError):
        fail_client.get('/example/20/')

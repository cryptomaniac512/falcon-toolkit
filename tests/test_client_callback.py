import pytest


def success_calllback(client, response):
    assert response.headers['Access-Control-Allow-Origin'] == '*'


@pytest.mark.client(callback=success_calllback)
def test_global_callback(client):
    client.get('/example/20/')


def fail_callback(client, response):
    assert response.headers['Access-Control-Allow-Origin'] == 'awesome.com'


@pytest.mark.client(callback=fail_callback)
def test_local_callback(client):
    with pytest.raises(AssertionError):
        client.get('/example/20/')

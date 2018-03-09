import pytest


def test_success(client):
    got = client.get('/example/20/')

    assert got == '20 ok'


def test_success_as_response(client):
    response = client.get('/example/20/', as_response=True)

    assert response.status_code == 200
    assert response.json == '20 ok'


def test_failed(client):
    with pytest.raises(AssertionError):
        client.get('/example/42/')


def test_failed_as_response(client):
    response = client.get('/example/42/', as_response=True)

    assert response.status_code == 400
    assert response.json == 'Invalid id'


def test_failed_with_default_client(default_client):
    """Will raise `KeyError` because `Origin` header is not provided"""
    with pytest.raises(KeyError):
        default_client.get('/example/20/')

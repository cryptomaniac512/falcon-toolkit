import pytest


def test_success(client):
    got = client.head('/example/20/')

    assert not got


def test_success_as_response(client):
    response = client.head('/example/20/', as_response=True)

    assert response.status_code == 200
    assert not response.content


def test_failed(client):
    with pytest.raises(AssertionError):
        client.head('/example/42/')


def test_failed_as_response(client):
    response = client.head('/example/42/', as_response=True)

    assert response.status_code == 400
    assert not response.content

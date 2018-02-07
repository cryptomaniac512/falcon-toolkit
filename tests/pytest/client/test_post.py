import pytest


def test_success(client):
    got = client.post('/example/', json={'id': 42})

    assert got == '42 created'


def test_success_as_response(client):
    response = client.post('/example/', json={'id': 42}, as_response=True)

    assert response.status_code == 201
    assert response.json == '42 created'


def test_failed(client):
    with pytest.raises(AssertionError):
        client.post('/example/', json={'id': 44})


def test_failed_as_response(client):
    response = client.post('/example/', json={'id': 44}, as_response=True)

    assert response.status_code == 400
    assert response.json == 'Invalid id'

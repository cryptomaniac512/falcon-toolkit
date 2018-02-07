import pytest


@pytest.mark.parametrize('id, data', (
    ('20', '20 deleted'),
    ('22', '22 accepted'),
    ('24', None),
))
def test_success(client, id, data):
    got = client.delete('/example/{}/'.format(id))

    assert got == data


@pytest.mark.parametrize('id, status, data', (
    ('20', 200, b'"20 deleted"'),
    ('22', 202, b'"22 accepted"'),
    ('24', 204, b''),
))
def test_success_as_response(client, id, status, data):
    response = client.delete('/example/{}/'.format(id), as_response=True)

    assert response.status_code == status
    assert response.content == data


def test_failed(client):
    with pytest.raises(AssertionError):
        client.delete('/example/42/')


def test_failed_as_response(client):
    response = client.delete('/example/42/', as_response=True)

    assert response.status_code == 400
    assert response.json == 'Invalid id'

import pytest


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_json(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    got = client.post('/example/', json={'id': 42})

    assert got == '42 created'


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_response(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    response = client.post('/example/', json={'id': 42}, as_response=True)

    assert response.status_code == 201
    assert response.json == '42 created'


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_raises_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    with pytest.raises(AssertionError):
        client.post('/example/', json={'id': 44})


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_response_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    response = client.post('/example/', json={'id': 44}, as_response=True)

    assert response.status_code == 400
    assert response.json == 'Invalid id'


def test_raises_with_default_client_for_cors_api(make_client, cors_api):
    """Will raise `KeyError` because `Origin` header is not provided by
    default client."""
    client = make_client(cors_api)

    with pytest.raises(KeyError):
        client.post('/example/', json={'id': 42})

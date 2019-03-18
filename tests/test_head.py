import pytest


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_json(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    got = client.head("/example/20/")

    assert not got


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_response(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    response = client.head("/example/20/", as_response=True)

    assert response.status_code == 200
    assert not response.content


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_raises_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    with pytest.raises(AssertionError):
        client.head("/example/42/")


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_response_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    response = client.head("/example/42/", as_response=True)

    assert response.status_code == 400
    assert not response.content


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_json_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    got = client.head("/example/42/", expected_statuses=[400])

    assert not got


def test_raises_with_default_client_for_cors_api(make_client, cors_api):
    """Will raise `KeyError` because `Origin` header is not provided by
    default client."""
    client = make_client(cors_api)

    with pytest.raises(KeyError):
        client.head("/example/20/")

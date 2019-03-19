import pytest


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
@pytest.mark.parametrize("id, data", (("20", "20 updated"), ("24", None)))
def test_getting_json(request, client_fixture, id, data):
    client = request.getfixturevalue(client_fixture)

    got = client.put("/example/{}/".format(id))

    assert got == data


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
@pytest.mark.parametrize(
    "id, status, data", (("20", 200, b'"20 updated"'), ("24", 204, b""))
)
def test_getting_response(request, client_fixture, id, status, data):
    client = request.getfixturevalue(client_fixture)

    response = client.put("/example/{}/".format(id), as_response=True)

    assert response.status_code == status
    assert response.content == data


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_raises_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    with pytest.raises(AssertionError):
        client.put("/example/42/")


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_response_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    response = client.put("/example/42/", as_response=True)

    assert response.status_code == 400
    assert response.json == "Invalid id"


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_json_for_failed_request(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    got = client.put("/example/42/", expected_statuses=[400])

    assert got == "Invalid id"


def test_raises_with_default_client_for_cors_api(make_client, cors_api):
    """Will raise `KeyError` because `Origin` header is not provided by
    default client."""
    client = make_client(cors_api)

    with pytest.raises(KeyError):
        client.put("/example/20/")

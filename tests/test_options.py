import pytest


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_json(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    got = client.options('/example/20/')

    assert not got


@pytest.mark.parametrize("client_fixture", ("client", "cors_client"))
def test_getting_response(request, client_fixture):
    client = request.getfixturevalue(client_fixture)

    response = client.options('/example/20/', as_response=True)

    assert response.status_code == 200
    assert not response.content

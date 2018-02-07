def test_success(client):
    got = client.options('/example/20/')

    assert not got


def test_success_as_response(client):
    response = client.options('/example/20/', as_response=True)

    assert response.status_code == 200
    assert not response.content

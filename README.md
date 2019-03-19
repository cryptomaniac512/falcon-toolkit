Pytest Falcon Client
===
Pytest `client` fixture for the [Falcon Framework](https://github.com/falconry/falcon).

[![Build Status](https://travis-ci.org/sivakov512/pytest-falcon-client.svg?branch=master)](https://travis-ci.org/sivakov512/pytest-falcon-client)
[![Coverage Status](https://coveralls.io/repos/github/sivakov512/pytest-falcon-client/badge.svg?branch=master)](https://coveralls.io/github/sivakov512/pytest-falcon-client?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![Python versions](https://img.shields.io/badge/python-3.6,%203.7-blue.svg)
[![PyPi](https://img.shields.io/pypi/v/pytest-falcon-client.svg)](https://pypi.python.org/pypi/pytest-falcon-client)

## Installation

``` shell
pip install pytest-falcon-client
```

## Setup

Plugin provides `make_client` fixture that you can use as is by passing `falcon.API` instance as argument:
``` python
import pytest

from yout_application import create_api

@pytest.fixture
def api():
    return create_api()


def test_something(make_client, api):
    client = make_client(api)

    got = client.get('/your_url/42/')

    assert got == {'awesome': 'response'}
```

For simpler usage you can define your own `client` fixture:
``` python
import pytest

from yout_application import create_api

@pytest.fixture
def client(make_client):
    api = create_api()
    return make_client(api)


def test_something(client):
    got = client.get('/your_url/42/')

    assert got == {'awesome': 'response'}
```

## Assertion examples

### Get response body as json and do automatic assertions for status code

``` python
def test_something(client):
    got = client.get('/your_url/42/')

    assert got == {'some': 'staff'}
```

### Get response body as json and do automatic assertions for your own status codes

``` python
def test_something(client):
    got = client.get('/your_url/42/', expected_statuses=[400, 401])

    assert got == {'some': 'stuff'}
```

### Get response object as is and skip any automatic assertions

``` python
def test_something(client):
    response = client.get('/your_url/42/', as_response=True)

    assert response.status_code == 400
    assert response.json == {'some': 'stuff'}
```

### Custom automatic assertions on every request

For example, you want to assert that every response has
`Access-Control-Allow-Origin` header with value `falconframework.org`.
You can do it with custom `ApiTestClient` like this:
``` python
import pytest

from pytest_falcon_client import ApiTestClient

from yout_application import create_api


class CustomApiTestClient(ApiTestClient):
    def response_assertions(self, response):
        # You can do any automatic assertions here for every request
        assert response.headers[
            'Access-Control-Allow-Origin'] == 'falconframework.org'


@pytest.fixture
def client():
    api = create_api()
    return CustomApiTestClient(api)


def test_something(client):
    response = client.get('/your_url/42/', as_response=True)

    assert response.status_code == 400
    assert response.json == {'some': 'stuff'}
```


### Simulate some default client behaviour

What if you service depends on some default client behaviour, like headers,
cookies or something else? You can setup this behaviour for every request
with custom `ApiTestClient`:
``` python
import pytest

from pytest_falcon_client import ApiTestClient

from yout_application import create_api


class CustomApiTestClient(ApiTestClient):
    def prepare_request(self, method, expected_statuses, *args, **kwargs):
        kwargs['headers'] = {'Origin': 'falconframework.org'}  # add `ORIGIN` header to every request
        return args, kwargs, expected_statuses  # should returns all of this


@pytest.fixture
def client():
    api = create_api()
    return CustomApiTestClient(api)


def test_something(client):
    got = client.get('/your_url/42/', as_response=True)

    assert got == {'some': 'stuff'}
```

Look at more examples in `tests`.

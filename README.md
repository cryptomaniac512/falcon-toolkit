Falcon Toolkit
===
Collection of utils for the [Falcon Framework](https://github.com/falconry/falcon).

[![Build Status](https://travis-ci.org/cryptomaniac512/falcon-toolkit.svg?branch=master)](https://travis-ci.org/cryptomaniac512/falcon-toolkit)
[![Coverage Status](https://coveralls.io/repos/github/cryptomaniac512/falcon-toolkit/badge.svg?branch=master)](https://coveralls.io/github/cryptomaniac512/falcon-toolkit?branch=master)
![Python versions](https://img.shields.io/badge/python-3.4,%203.5,%203.6-blue.svg)

## Installation

``` python
pip install falcon-toolkit
```

## Provided fixtures

Before using it you must define `api` that returns instance of your `falcon.API` app

``` python
import pytest

from yout_application import create_api

@pytest.fixture
def api():
    return create_api()
```

### client

``` python
def test_something(client):
    got = client.get('/your_url/42/')  # returns json of response and automatically check response status code
	assert got == {'awesome': 'response'}

	response = client.get('/your_url/100500/')  # returns testing response object and skip status code check
	assert response.status_code == 400
	assert response.json = 'Invalid id'
```

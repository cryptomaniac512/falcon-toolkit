from falcon import testing


class ApiTestClient(testing.TestClient):

    _method_to_statuses = {
        'DELETE': [200, 202, 204],
        'GET': [200],
        'HEAD': [200],
        'OPTIONS': [200],
        'POST': [201],
        'PUT': [200, 204],
    }

    def delete(self, *args, **kwargs):
        expected = self._method_to_statuses['DELETE']
        return self._process_request('DELETE', expected, *args, **kwargs)

    def get(self, *args, **kwargs):
        expected = self._method_to_statuses['GET']
        return self._process_request('GET', expected, *args, **kwargs)

    def head(self, *args, **kwargs):
        expected = self._method_to_statuses['HEAD']
        return self._process_request('HEAD', expected, *args, **kwargs)

    def options(self, *args, **kwargs):
        expected = self._method_to_statuses['OPTIONS']
        return self._process_request('OPTIONS', expected, *args, **kwargs)

    def post(self, *args, **kwargs):
        expected = self._method_to_statuses['POST']
        return self._process_request('POST', expected, *args, **kwargs)

    def put(self, *args, **kwargs):
        expected = self._method_to_statuses['PUT']
        return self._process_request('PUT', expected, *args, **kwargs)

    def prepare_request(self, method, expected, *args, **kwargs):
        return args, kwargs

    def response_assertions(self, response):
        pass  # pragma: no cover

    def _process_request(self, method, expected, *args, **kwargs):
        args, kwargs = self.prepare_request(
            method, expected, *args, **kwargs)

        as_response = kwargs.pop('as_response', False)

        response = self.simulate_request(method, *args, **kwargs)

        self.response_assertions(response)

        if as_response:
            return response

        assert response.status_code in expected

        if response.content:
            return response.json

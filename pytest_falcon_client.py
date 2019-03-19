from typing import Any, List, Optional, Tuple, Union

import pytest
from falcon import testing


class ApiTestClient(testing.TestClient):

    _method_to_statuses = {
        "DELETE": [200, 202, 204],
        "GET": [200],
        "HEAD": [200],
        "OPTIONS": [200],
        "POST": [201],
        "PUT": [200, 204],
    }

    def prepare_request(
        self, method: str, expected_statuses: List[str], *args, **kwargs
    ) -> Tuple[tuple, dict, List[str]]:
        return args, kwargs, expected_statuses

    def __getattr__(self, name: str):
        return lambda *a, **kw: self._process_request(name.upper(), *a, **kw)

    def response_assertions(self, response: testing.Result):
        pass  # pragma: no cover

    def _process_request(
        self,
        method: str,
        path: str = "/",
        expected_statuses: List[int] = None,
        as_response: bool = False,
        *args,
        **kwargs,
    ) -> Optional[Union[Any, testing.Result]]:
        args, kwargs, expected_statuses = self.prepare_request(
            method,
            expected_statuses or self._method_to_statuses.get(method, []),
            *args,
            **kwargs,
        )

        response = self.simulate_request(
            method=method, path=path, *args, **kwargs
        )

        self.response_assertions(response)

        if as_response:
            return response

        if expected_statuses:
            assert response.status_code in expected_statuses

        if response.content:
            return response.json


@pytest.fixture
def make_client():
    return lambda api: ApiTestClient(api)

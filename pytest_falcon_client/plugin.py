import falcon
import pytest

from .client import ApiTestClient


class FalconClientPlugin:

    def __init__(self):
        self.callback = None

    @pytest.fixture(name='client')
    def client_fixture(self, api: falcon.API):
        yield ApiTestClient(api, _callback=self.callback)

    @pytest.hookimpl(tryfirst=True)
    def pytest_runtest_setup(self, item):
        mark = item.get_marker('client')
        if mark:
            self.callback = mark.kwargs.get('callback', None)

    @pytest.hookimpl(trylast=True)
    def pytest_runtest_teardown(self):
        self.callback = None


plugin = FalconClientPlugin()

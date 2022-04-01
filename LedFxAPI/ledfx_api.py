from .api import API
from .api_helpers import APIHelpers


class LedFxApi:
    def __init__(self, host, port, https=False):
        self.api = API(host, port, https)
        self.helper = APIHelpers(self.api)

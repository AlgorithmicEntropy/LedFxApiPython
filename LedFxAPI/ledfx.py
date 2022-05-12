from .raw_api import RawAPI
from .api_helpers import APIHelpers


class LedFx:
    def __init__(self, host, port, ssl=False):
        self.api = RawAPI(host, port, ssl)
        self.helper = APIHelpers(self.api)

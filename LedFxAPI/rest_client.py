import logging
import urllib.parse as url_parser

import asyncio
import aiohttp
import json

_LOGGER = logging.getLogger(__name__)


class ApiError(BaseException):
    pass


class RESTClient:
    def __init__(self, host, port, url_base, https=False, ):
        if https:
            self.base_url = f"https://{host}:{port}"
        else:
            self.base_url = f"http://{host}:{port}"

        self.base_url = url_parser.urljoin(self.base_url, url_base)

    """
    @staticmethod
    def handle_exception(e, response):
        if isinstance(e, requests.ConnectionError):
            _LOGGER.error("Cant connect to LedFx Instance")
        if isinstance(e, requests.HTTPError):
            # Handle http errors
            _LOGGER.error(response.text)
        if isinstance(e, requests.Timeout):
            _LOGGER.error("Timeout while connecting to LedFx Instance")
        if isinstance(e, requests.TooManyRedirects):
            _LOGGER.error("To many redirects while connecting to LedFx Instance")

        raise ApiError from e
    """

    def handle_http_error(self, e):
        pass

    async def get(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :return: json response as dict obj
        """
        url = url_parser.urljoin(self.base_url, path)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=headers, data=json.dumps(data)) as resp:
                    return await resp.json()
            except Exception as e:
                # self.handle_exception(e, response)
                pass

    async def post(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :returns:
            - json response as dict obj
        """
        url = url_parser.urljoin(self.base_url, path)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, headers=headers, data=json.dumps(data)) as resp:
                    return await resp.json()
            except Exception as e:
                # self.handle_exception(e, response)
                pass

    async def put(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :returns:
            - json response as dict obj
        """
        url = url_parser.urljoin(self.base_url, path)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.put(url, headers=headers, data=json.dumps(data)) as resp:
                    return await resp.json()
            except Exception as e:
                # self.handle_exception(e, response)
                pass

    async def delete(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :returns:
            - json response as dict obj
        """
        url = url_parser.urljoin(self.base_url, path)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.delete(url, headers=headers, data=json.dumps(data)) as resp:
                    return await resp.json()
            except Exception as e:
                # self.handle_exception(e, response)
                pass

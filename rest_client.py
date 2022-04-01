import logging
import urllib.parse as url_parser

import requests
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

    def handle_http_error(self, e):
        pass

    def get(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :return: json as dict
        """
        url = url_parser.urljoin(self.base_url, path)
        response = None
        try:
            response = requests.request('GET', url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.handle_exception(e, response)

    def post(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :returns:
            - json - json as dict
            - status - status code
        """
        url = url_parser.urljoin(self.base_url, path)
        response = None
        try:
            response = requests.request('POST', url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.RequestException as e:
            self.handle_exception(e, response)

    def put(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :returns:
            - json - json as dict
            - status - status code
        """
        url = url_parser.urljoin(self.base_url, path)
        response = None
        try:
            response = requests.request('PUT', url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.RequestException as e:
            self.handle_exception(e, response)

    def delete(self, path, data=None, headers=None):
        """
        :param path: url path
        :param data: dict like obj
        :param headers: request headers
        :returns:
            - json - json as dict
            - status - status code
        """
        url = url_parser.urljoin(self.base_url, path)
        response = None
        try:
            response = requests.request('DEL', url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.RequestException as e:
            self.handle_exception(e, response)

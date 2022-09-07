from urllib.parse import urlparse

import requests
import urllib3
from colorama import Fore

from lib.response import Response

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Forwarder:

    def __init__(self, url: str, headers: dict, method: str, body):
        self._url = url
        self._headers = self._fix_headers(headers)
        self._method = method
        self._body = body

    def forward(self) -> Response | None:
        response = None

        if self._method == "GET":
            response = self._get()
        elif self._method == "POST":
            response = self._post()
        elif self._method == "HEAD":
            response = self._head()

        if response is not None:
            return Response(response.text, response.status_code, response.headers, self._url, self._method)
        else:
            print(f"{Fore.RED}[-] HTTP method {self._method} is not implemented")
            return None

    def _get(self):
        return requests.get(self._url, verify=False, data=self._body,
                            proxies={'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'})

    def _post(self):
        return requests.post(self._url, verify=False, data=self._body, headers=self._headers,
                             proxies={'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'})

    def _head(self):
        return requests.head(self._url, verify=False, data=self._body,
                             proxies={'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'})

    def _fix_headers(self, headers: dict) -> dict:
        for header in headers:
            if header.upper() == 'HOST':
                url_parsed = urlparse(self._url)
                headers[header] = url_parsed.hostname

                if url_parsed.port:
                    header[header] += f":{url_parsed.port}"

        return headers

import requests

from lib.response import Response


class Forwarder:

    def __init__(self, url: str, headers: {}, method: str):
        self._url = url
        self._headers = headers
        self._method = method

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
            print(f"[-] HTTP method {self._method} is not implemented")
            return None

    def _get(self):
        return requests.get(self._url)

    def _post(self):
        return requests.post(self._url)

    def _head(self):
        return requests.head(self._url)

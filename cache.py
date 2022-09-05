from response import Response


class Cache:

    def __init__(self):
        self._entries = {}

    def has(self, url, method):
        if method not in self._entries:
            return False

        if url not in self._entries[method]:
            return False

        return True

    def get(self, url, method) -> Response | None:
        if self.has(url, method):
            return self._entries[method][url]['response']
        else:
            return None


    def store(self, response: Response):
        method = response.get_request_method()
        url = response.get_request_url()

        if method not in self._entries:
            self._entries[method] = {}

        self._entries[method][url] = {
            "response": response
        }

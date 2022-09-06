class Response:

    def __init__(self, content: str, status: int, headers, request_url, request_method):
        self._content = content
        self._status = status
        self.request_url = request_url
        self.request_method = request_method
        self._headers = {}

        for key in headers:
            if key == 'Transfer-Encoding':
                self._headers['Content-Length'] = len(content.encode())
                continue

            self._headers[key] = headers[key]

    def get_content(self):
        return self._content

    def get_request_url(self):
        return self.request_url

    def get_request_method(self):
        return self.request_method

    def get_status(self):
        return self._status

    def get_headers(self):
        return self._headers

    def build(self):
        # Add the first line
        lines = [f"HTTP/1.1 {self._status}"]

        # Add response headers
        for key in self._headers:
            lines.append(f"{key}: {self._headers[key]}")

        # Add break before body
        lines.append("")

        lines.append(self._content)

        # Add break before body
        lines.append("")

        return '\r\n'.join(lines).encode()

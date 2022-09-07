from colorama import Fore

from lib.cache import Cache
from lib.forwarder import Forwarder
from lib.parser import get_method, get_url, get_headers, get_body


class Client:

    def __init__(self, socket, cache: Cache):
        self._socket = socket
        self._cache = cache

    def handle_connection(self):
        request = self._socket.recv(1024).decode()

        self.process_request(request)

    def process_request(self, request):
        url = get_url(request)
        method = get_method(request)
        headers = get_headers(request)
        body = get_body(request)

        if self._cache.has(url, method):
            print(f"{Fore.GREEN}[+] Cache {method} {url}")
            self._socket.sendall(self._cache.get(url, method).build())
        else:
            print(f"{Fore.YELLOW}[+] Forwarding {method} {url}")

            response = Forwarder(url, headers, method, body).forward()

            if response is not None:
                self._cache.store(response)
                self._socket.sendall(response.build())

        self._socket.close()

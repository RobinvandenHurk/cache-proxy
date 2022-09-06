import socket

import colorama
from colorama import Fore

from lib.cache import Cache
from lib.client import Client


class Server:

    def __init__(self, port):
        self._cache = Cache()
        self._port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('0.0.0.0', port))
        self.socket.listen(1)

    def start(self):
        colorama.init()
        print(f"{Fore.CYAN}[*] Started Caching Proxy on port {self._port}")

        while True:
            client_socket, client_address = self.socket.accept()
            client = Client(client_socket, self._cache)
            client.handle_connection()

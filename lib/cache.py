import os.path

import jsonpickle
from colorama import Fore

from lib.response import Response


class Cache:

    def __init__(self, session_file=None):
        self._session_file = session_file
        self.cache_entries = {}

        if session_file:
            self._load_session()

    def get_all(self):
        return self.cache_entries

    def has(self, url, method):
        if method not in self.cache_entries:
            return False

        if url not in self.cache_entries[method]:
            return False

        return True

    def get(self, url, method) -> Response | None:
        if self.has(url, method):
            return self.cache_entries[method][url]['response']
        else:
            return None

    def store(self, response: Response):
        method = response.get_request_method()
        url = response.get_request_url()

        if method not in self.cache_entries:
            self.cache_entries[method] = {}

        self.cache_entries[method][url] = {
            "response": response
        }

        if self._session_file:
            # TODO: Only store all entries once session is ended
            #  Not doing that now because lots of issues with sharing
            #  The cache instance between threads
            with open(self._session_file, "w") as session_file:
                session_file.write(jsonpickle.encode(self.cache_entries))

    def _load_session(self):
        if self._session_file:
            if os.path.isfile(self._session_file):

                with open(self._session_file, "r") as session_file:
                    self.cache_entries = jsonpickle.decode(session_file.read())

                    total = sum(int(v) for v in [len(self.cache_entries[entry]) for entry in self.cache_entries])

                    print(
                        f"{Fore.GREEN}[+] Successfully loaded {total} cache entries from previous session")
            else:
                print(f"{Fore.GREEN}[+] Using session file '{self._session_file}'")

import sys
from multiprocessing import Process

import colorama
from colorama import Fore

from lib.cache import Cache
from lib.server import Server

if __name__ == '__main__':
    colorama.init()
    cache = Cache()
    thread = Process(target=Server(5000).start)
    thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print(f"{Fore.CYAN}[*] Stopping Caching Proxy")
        thread.kill()
        sys.exit(0)

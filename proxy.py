import argparse
import sys
from multiprocessing import Process

import colorama
from colorama import Fore

from lib.cache import Cache
from lib.server import Server

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Your local caching proxy')
    parser.add_argument('-s', dest='session_file', type=str, help='Use session file')

    args = parser.parse_args()

    colorama.init()
    cache = Cache(args.session_file)
    process = Process(target=Server(5000, cache).start)
    process.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print(f"{Fore.CYAN}[*] Stopping Caching Proxy")
        process.kill()
        sys.exit(0)

#!/usr/bin/python3
"""#!/usr/bin/python3"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        link = urllib.request.Request(argv[1])
        with urllib.request.urlopen(link) as response:
            print(response.getheader('X-Request-Id'))

#!/usr/bin/python3
"""script that sends a request to the specified URL
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as response:
            header_value = response.info().get("X-Request-Id")
            if header_value:
                print(header_value)

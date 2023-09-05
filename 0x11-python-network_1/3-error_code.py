#!/usr/bin/python3
"""Script that sends a request to a URL and displays the body of the response.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        try:
            with urllib.request.urlopen(url) as response:
                body = response.read()
                print(body.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")

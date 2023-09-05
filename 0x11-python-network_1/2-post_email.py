#!/usr/bin/python3
"""Script that sends a POST request to a specified URL with an email parameter
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='POST')

        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))

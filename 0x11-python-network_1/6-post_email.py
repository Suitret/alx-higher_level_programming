#!/usr/bin/python3
"""
Python script that sends a POST request to a specified URL with an email
parameter and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        payload = {'email': email}
        response = requests.post(url, data=payload)

        print(response.text)

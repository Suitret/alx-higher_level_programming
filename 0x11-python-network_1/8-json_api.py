#!/usr/bin/python3
"""
Python script that sends a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter and displays the response accordingly.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

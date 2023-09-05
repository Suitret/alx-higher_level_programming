#!/usr/bin/python3
"""
Python script that uses the GitHub API to display your GitHub user ID.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        pat = sys.argv[2]

        # Create a Basic Authentication string using your PAT as the password
        auth = (username, pat)

        # Define the GitHub API endpoint for user information
        url = 'https://api.github.com/user'

        try:
            # Send a GET request to the GitHub API with Basic Authentication
            response = requests.get(url, auth=auth)
            data = response.json()

            if 'id' in data:
                print(data['id'])
            else:
                print("None")
        except requests.exceptions.RequestException as e:
            print("None")
    else:
        print("None")

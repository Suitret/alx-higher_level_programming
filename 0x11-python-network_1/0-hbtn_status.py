#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body_response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_response)))
        print("\t- content: {}".format(body_response))
        print("\t- type: {}".format(body_response

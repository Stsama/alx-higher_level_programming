#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter"""


if __name__ == "__main__":
    import sys
    import requests
    email = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=email)
    print(req.text)

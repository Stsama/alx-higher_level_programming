#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the"""


if __name__ == "__main__":
    import sys
    import urllib.request
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))

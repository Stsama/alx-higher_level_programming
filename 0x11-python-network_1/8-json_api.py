#!/usr/bin/python3
"""
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
if __name__ == "__main__":
    import sys
    import requests
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    value = {"q": letter}

    req = requests.post("http://0.0.0.0:5000/search_user", data=value)

    try:
        result = req.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""Sends a POST request with a letter and displays JSON result."""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        j = r.json()
        if j:
            print("[{}] {}".format(j.get('id'), j.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")

#!/usr/bin/python3
"""Sends a POST request with email parameter and displays the response body."""
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)

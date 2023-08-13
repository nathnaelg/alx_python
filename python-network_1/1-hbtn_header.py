#!/usr/bin/python3
"""A script for fetches https://alx-intranet.hbtn.io/status status
"""
import requests

if __name__ == '__main__':

    url = 'https://alx-intranet.hbtn.io/status'
    result = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))

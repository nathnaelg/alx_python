#!/usr/bin/python3
"""post module"""

import sys
import requests

if __name__ == '__main__':
    """ script that takes in a URL and
        an email address, sends a POST request
        to the passed URL with the email as
        a parameter
    """
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    response = requests.post(url, data=email)

    print("Your email is: {:}".format(response.text))

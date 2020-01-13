#!/usr/bin/python3
# Display the status
import requests


if __name__ == "__main__":

    result = requests.get('https://intranet.hbtn.io/status')
    print(result.headers['X-Request-Id'])

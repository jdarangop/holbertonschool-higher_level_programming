#!/usr/bin/python3
# Display the status
import requests
import sys


if __name__ == "__main__":

    result = requests.get(sys.argv[1])
    print(result.headers['X-Request-Id'])

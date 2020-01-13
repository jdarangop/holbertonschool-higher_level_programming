#!/usr/bin/python3
# Display header X-Request-Id
import urllib.request
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))

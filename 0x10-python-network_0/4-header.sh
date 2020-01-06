#!/bin/bash
# Takes a specific header value
curl -s -L "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"

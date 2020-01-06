#!/bin/bash
# Takes bytes from body request
curl -s -f -L "$1" -X GET

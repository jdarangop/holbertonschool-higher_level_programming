#!/bin/bash
# Takes bytes from body request
curl -s -o "$1" -w "%{size_download}"

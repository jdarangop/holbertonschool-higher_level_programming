#!/bin/bash
# Takes delete request
curl -sD - -o /dev/null "$1" | grep "Allow" | cut -d ":" -f2 | cut -b 2- 

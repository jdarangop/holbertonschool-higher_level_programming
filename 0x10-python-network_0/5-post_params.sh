#!/bin/bash
# Takes a specific values using POST
curl -s -L "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

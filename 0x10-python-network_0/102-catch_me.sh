#!/bin/bash
# Solve catch me
curl -s -L 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"

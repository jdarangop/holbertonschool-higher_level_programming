#!/usr/bin/python3
# Star wars API
import requests
import sys


if __name__ == "__main__":

    arg = sys.argv[1]
    value = {'search': arg}
    result = requests.get("https://swapi.co/api/people/?search=r2",
                          params=value)

    dict_data = result.json()
    print("Number of results: {}".format(dict_data["count"]))
    for i in dict_data["results"]:
        print(i["name"])

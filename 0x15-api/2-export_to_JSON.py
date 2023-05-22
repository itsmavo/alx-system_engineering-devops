#!/usr/bin/python3
"""Returns to-do list information for a given employee id"""
import requests
import sys
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    to_do = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        json.dump({sys.argv[1]: [{
            "task": td.get("title"),
            "completed": td.get("completed"),
            "username": username
            } for td in to_do]}, jsonfile)

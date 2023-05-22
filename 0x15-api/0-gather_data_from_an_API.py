#!/usr/bin/python3
"""Returns to-do list information for a given employee id"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done = [td.get("title") for td in todo if td.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todo)))
    [print("/t {}".format(d)) for d in done]

#!/usr/bin/python3
"""Exports to-do list info for a given employee ID to CSV"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    to_do = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        wrt = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [wrt.writerow(
            [sys.argv[1], username, td.get("completed"), td.get("title")]
            ) for td in to_do]

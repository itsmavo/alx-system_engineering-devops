#!/usr/bin/python3
""" Exports todo list info of all employees to JSON file"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": u.get("username")
                } for td in requests.get(url + "todos",
                    params={"userId":u.get("id")}).json()]
                for u in users}, jsonfile)

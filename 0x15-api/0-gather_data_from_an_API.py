#!/usr/bin/python3
"""
for a given employee ID,
returns information about his/her TODO list progress
"""

from sys import argv
import json
import requests


def get_todos(user_id):
    """ nformation about their TODO list progress"""

    url = "https://jsonplaceholder.typicode.com/users"

    user = requests.get(f"{url}/{user_id}")
    todos = requests.get(f"{url}/{user_id}/todos")
    todos_complete = requests.get(f"{url}/{user_id}/todos?completed=true")
    user_name = user.json().get('name')
    total_task = len(todos.json())
    complete_task = len(todos_complete.json())

    print(f"Employee {user_name} is done \
with tasks({complete_task}/{total_task}):")
    for i in todos_complete.json():
        print(f"\t {i.get('title')}")


if __name__ == "__main__":
    if argv[1]:
        get_todos(argv[1])

#!/usr/bin/python3
""" Script to get information about employee"""

import json
import requests
from sys import argv


def get_todos():
    """ get information about all users """

    url = "https://jsonplaceholder.typicode.com/users"

    dict_user = {}
    users = requests.get(f"{url}").json()
    for user in users:
        user_name = user.get('username')
        user_id = user.get('id')
        todos = requests.get(f"{url}/{user_id}/todos")
        list_task = []
        for i in todos.json():
            dict_task = {"username": user_name,
                         "task": i.get('title'),
                         "completed": i.get('completed'),
                         }
            list_task.append(dict_task)
        dict_user[f"{user_id}"] = list_task

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_user, file)


if __name__ == "__main__":
    get_todos()

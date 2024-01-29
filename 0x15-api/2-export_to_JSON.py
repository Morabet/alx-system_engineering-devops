#!/usr/bin/python3
""" Script to export data in the JSON format """

import csv
from sys import argv
import json
import requests


def get_todos(user_id):
    """ get information about user by id"""

    url = "https://jsonplaceholder.typicode.com/users"

    user = requests.get(f"{url}/{user_id}")
    todos = requests.get(f"{url}/{user_id}/todos")
    user_name = user.json().get('username')
    user_id = user.json().get('id')

    list_task = []
    for i in todos.json():
        dict_task = {"task": i.get('title'),
                     "completed": i.get('completed'),
                     "username": user_name
                     }
        list_task.append(dict_task)

    dict_user = {f"{user_id}": list_task}
    with open(f"{user_id}.json", "w") as file:
        json.dump(dict_user, file)


if __name__ == "__main__":
    if argv[1]:
        get_todos(argv[1])

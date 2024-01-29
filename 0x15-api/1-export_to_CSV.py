#!/usr/bin/python3
""" Script to export data in the CSV format"""

import csv
import json
import requests
from sys import argv


def get_todos(user_id):
    """get data in the CSV format """

    url = "https://jsonplaceholder.typicode.com/users"

    user = requests.get(f"{url}/{user_id}")
    todos = requests.get(f"{url}/{user_id}/todos")
    u_name = user.json().get('username')
    u_id = user.json().get('id')

    with open(f"{user_id}.csv", "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in todos.json():
            writer.writerow([u_id, u_name, i.get('completed'), i.get('title')])


if __name__ == "__main__":
    if argv[1]:
        get_todos(argv[1])

#!/usr/bin/python3
'''API module'''
import json
import requests
import sys


if __name__ == '__main__':
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/').json()

    json_db = {}
    for user in users:
        user_id = str(user.get('id'))

        info = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId=' +
            user_id).json()

        json_db[user_id] = [{
            "username": user.get('username'),
            "task": task.get("title"),
            "completed": task.get("completed")
            } for task in info]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(json_db, f)

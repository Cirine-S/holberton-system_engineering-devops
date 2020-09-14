#!/usr/bin/python3
'''API module'''
import csv
import requests
import sys


def to_csv(employee_id):
    ''' Using a given REST API, for a given employee ID,
    returns information about his/her TODO list progress'''

    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + employee_id).json()['username']

    info = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id).json()

    js = {employee_id: [{
        for task in info:
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employee_name
                    } for task in info]}
    # write json
    with open('{}.json'.format(_id), 'w') as json_file:
        json_file.write(json.dumps(j_output))


if __name__ == '__main__':
    employee_id = sys.argv[1]
    to_csv(employee_id)

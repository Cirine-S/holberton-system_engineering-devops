#!/usr/bin/python3
'''API module'''
import json
import requests
import sys


def to_csv(employee_id):
    ''' Using a given REST API, for a given employee ID,
    returns information about his/her TODO list progress'''

    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + employee_id).json()['username']

    info = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id).json()

    data = {employee_id: []}
    for task in info:
        new_dic = {}
        new_dic["task"] = task.get('title')
        new_dic["completed"] = task.get('completed')
        new_dic["username"] = employee_name
        data[employee_id].append(new_dic)

    # write json
    with open('{}.json'.format(employee_id), 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    employee_id = sys.argv[1]
    to_csv(employee_id)

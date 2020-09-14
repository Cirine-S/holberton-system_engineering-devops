#!/usr/bin/python3
'''API module'''
import json
import requests
import sys


def to_csv(empl_id):
    ''' Using a given REST API, for a given employee ID,
    returns information about his/her TODO list progress'''

    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + empl_id).json()
    employee_name = employee_name['username']

    info = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + empl_id).json()

    data = {empl_id: []}
    for task in info:
        new_dic = {}
        new_dic["task"] = task.get('title')
        new_dic["completed"] = task.get('completed')
        new_dic["username"] = employee_name
        data[empl_id].append(new_dic)

    # write json
    with open('{}.json'.format(empl_id), 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    empl_id = sys.argv[1]
    to_csv(empl_id)

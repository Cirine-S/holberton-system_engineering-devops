#!/usr/bin/python3
'''API module'''
import csv
import requests
import sys


def to_csv(empl_id):
    ''' Using a given REST API, for a given employee ID,
    returns information about his/her TODO list progress'''

    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + empl_id).json()
    employee_name = employee_name['name']

    info = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + empl_id).json()

    with open('{}.csv'.format(empl_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in info:
            writer.writerow([
                empl_id,
                employee_name,
                task.get('completed'),
                task.get('title')
                ])


if __name__ == '__main__':
    empl_id = sys.argv[1]
    to_csv(empl_id)

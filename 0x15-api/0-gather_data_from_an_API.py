#!/usr/bin/python3
'''API module'''
import requests
import sys


def todolist_progress(emp_id):
    ''' Using a given REST API, for a given employee ID,
    returns information about his/her TODO list progress'''

    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + emp_id).json()['name']

    info = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + emp_id).json()

    done_tasks = 0
    total_tasks = 0
    titles = []
    for task in info:
        if task.get("completed"):
            titles.append(task.get("title"))
            done_tasks += 1
        total_tasks += 1
    print(
        'Employee ' + employee_name + ' is done with tasks(' +
        str(done_tasks) + '/' + str(total_tasks) + '):')
    for title in titles:
        print('\t ' + title)


if __name__ == '__main__':
    emp_id = sys.argv[1]
    todolist_progress(emp_id)

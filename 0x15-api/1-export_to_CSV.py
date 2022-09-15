#!/usr/bin/python3
"""Script interacts with API to retrieve and present data"""


if __name__ == '__main__':
    import csv
    import json
    from requests import get
    from sys import argv

    emp_id = argv[1]

    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(emp_id))\
        .json()
    EMPLOYEE_NAME = user.get('name')

    todos = get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(emp_id)).json()

    with open('USER_ID.csv', 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            line = [
                task.get('userId'),
                user.get('username'),
                task.get('completed'),
                task.get('title')
                ]
            writer.writerow(line)

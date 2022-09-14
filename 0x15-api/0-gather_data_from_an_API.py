#!/usr/bin/python3
"""Script interacts with API to retrieve and present data"""


def task_inquiry():
    """Get and print data about employees and their responsibilities"""
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

    TOTAL_NUMBER_OF_TASKS = len(todos)

    done = []
    for task in todos:
        if (task.get('completed') is True):
            done.append(task)

    NUMBER_OF_DONE_TASKS = len(done)

    print(
        'Employee {} is done with tasks({}/{}):'
        .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    )

    [print('    {}'.format(task.get('title'))) for task in done]


if __name__ == '__main__':
    task_inquiry()

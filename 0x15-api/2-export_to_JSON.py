#!/usr/bin/python3
"""Script interacts with API to retrieve and present data"""


if __name__ == '__main__':
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

    todos_formatted = []
    for task in todos:
        todos_formatted.append(
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user.get('username')
            }
        )

    tasks_dict = {user.get('id'): todos_formatted}

    with open('{}.json'.format(emp_id), 'w+', newline='') as f:
        json.dump(tasks_dict, f)

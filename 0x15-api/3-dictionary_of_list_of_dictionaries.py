#!/usr/bin/python3
"""Script interacts with API to retrieve and present data"""


if __name__ == '__main__':
    import json
    from requests import get
    from sys import argv

    users = get('https://jsonplaceholder.typicode.com/users').json()
    tasks_dict = {}

    for user in users:
        todos = get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user.get('id'))).json()

        todos_formatted = []
        for task in todos:
            todos_formatted.append(
                {
                    'username': user.get('username'),
                    'task': task.get('title'),
                    'completed': task.get('completed')
                }
            )

        tasks_dict[user.get('id')] = todos_formatted

    with open('todo_all_employees.json', 'w+', newline='') as f:
        json.dump(tasks_dict, f)

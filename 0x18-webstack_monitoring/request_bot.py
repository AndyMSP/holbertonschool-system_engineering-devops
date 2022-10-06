#!/usr/bin/python3

import requests
import uuid

for i in range(1000):
    id = uuid.uuid4()
    params = {'id': id}
    res = requests.get('http://web-01.tacobell.tech', params=params)
    print(f'{i}: {res.status_code}')
    print(res.request.url)

print('done with 1000 requests')
#!/usr/bin/python3
"""Return hottest 10 posts of a subreddit"""


def top_ten(subreddit):
    """print hottest 10 posts in a subreddit"""
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'andy'}
    params = {'limit': '10'}
    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
        )

    if (res.status_code != 200):
        print('None')
    else:
        for post in res.json()['data']['children']:
            print(post['data']['title'])

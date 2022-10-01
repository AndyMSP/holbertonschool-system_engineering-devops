#!/usr/bin/python3
"""recursively finds number of hot posts in a subreddit"""


def recurse(subreddit, hot_list=[], after='blank'):
    """recursively finds number of hot posts in a subreddit"""
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'andy'}
    params = {'limit': '100', 'after': after}
    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
        )

    if (res.status_code != 200):
        return (None)
    elif (after is None):
        for post in res.json()['data']['children']:
            hot_list.append(post['data']['title'])
        return (hot_list)
    else:
        for post in res.json()['data']['children']:
            hot_list.append(post['data']['title'])
        after = res.json()['data']['after']
        return (recurse(subreddit, hot_list=hot_list, after=after))

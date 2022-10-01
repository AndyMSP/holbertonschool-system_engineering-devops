#!/usr/bin/python3
"""Use reddit api to get info about subredit subscribers"""


def number_of_subscribers(subreddit):
    """Return number of subscribers in subreddit given as argument"""
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'andy'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return (0)
    else:
        return (res.json()['data']['subscribers'])

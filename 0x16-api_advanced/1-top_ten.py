#!/usr/bin/python3
"""
subreddit module
"""
import requests


def top_ten(subreddit):
    """ function top_ten"""
    header = {'User-agent': 'Cirine'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'

    r = requests.get(url, headers=header, allow_redirects=False).json()
    try:
        for i in range(10):
            path = r.get('data').get('children')
            print(path[i].get('data').get('title'))
        return
    except Exception:
        pass
    print(None)
    return

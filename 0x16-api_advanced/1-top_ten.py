#!/usr/bin/python3
"""
subreddit module
"""
import requests


def top_ten(subreddit):
    """ function top_ten"""
    header = {'User-agent': 'Cirine'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'

    r = requests.get(url, headers=header)
    if r.status_code != 200:
        print(None)
        return
    path = r.json().get('data').get('children')
    for i in range(10):
        print(path[i].get('data').get('title'))

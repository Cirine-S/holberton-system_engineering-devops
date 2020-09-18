#!/usr/bin/python3
"""
subreddit module
"""
import requests


def number_of_subscribers(subreddit):
    '''returns the number of suscribers'''
    header = {'User-agent': 'Cirine'}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'

    r = requests.get(url, headers=header)
    if r.status_code != 200:
        return 0
    data = r.json()
    return(data.get('data').get('subscribers'))

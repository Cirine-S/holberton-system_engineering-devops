#!/usr/bin/python3
"""
subreddit module
"""


def number_of_subscribers(subreddit):
    '''returns the number of suscribers'''
    header = {UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

    URL = 'https://www.reddit.com/r/'+subreddit+'/about.json'
    r = requests.get(URL, headers=header)
    if r.status_code != 200:
        return 0
    data = r.json()
    return(data.get('data').get('subscribers'))

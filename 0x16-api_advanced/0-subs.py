#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64; en-US) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/49.0.2225.317 Safari/602'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs

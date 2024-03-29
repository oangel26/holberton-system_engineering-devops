#!/usr/bin/python3
""" Query subs """
import json
import requests

REDDIT_URL = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[], after=None):
    """ Get all posts via recursion """
    headers = {"User-Agent": "losky"}
    params = {"limit": 50}
    if isinstance(after, str):
        if after != "THEEND":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(REDDIT_URL.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'THEEND')
    if not after:
        after = "THEEND"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)

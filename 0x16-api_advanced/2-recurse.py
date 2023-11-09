#!/usr/bin/python3
"""
returns list containing the title of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], page_2=None, count=0):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if page_2:
        url += '?after={}'.format(page_2)
    headers = {'User-Agent': 'Shovi'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return None
    # python dict from json oblect
    data = res.json()['data']

    # get lists of pages
    posts = data['children']
    for post in posts:
        count = count + 1
        hot_list.append(post['data']['title'])

    page_2 = data['after']
    if page_2 is not None:
        return recurse(subreddit, hot_list, page_2, count)
    else:
        return hot_list

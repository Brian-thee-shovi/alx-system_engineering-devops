#!/usr/bin/python3
"""
module that queries the REDDIT API and returns
the number of total subs
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # it identifies source of the HTTP request to the Reddit servers

    my_headers = {'User-Agent': 'Shovi'}
    resq = requests.get(url, my_headers=headers)

    if resq.status_code == 200:
        data = resq.json()

        return data['data']['subscribers']
    else:
        return 0

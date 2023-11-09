#!/usr/bin/python3
"""
module queries the Reddit API and prints the titles of
1st ten hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """TOP 10 hots posts"""
    resq = requests.request(
         'GET',
         'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
         headers={
             'User-Agent': 'Shovi'
         },
         allow_redirects=False
    )

    if resq.status_code == 200:
        try:
            posts = resq.json().get('data').get('children')

            [print(post.get('data').get('title')) for post in posts]
        except Exception:
            pass
    else:
        print(None)

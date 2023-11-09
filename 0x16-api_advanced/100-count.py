#!/usr/bin/python3
"""
Queries the API, parses the title of all hot articles,
and prints a sorted count
"""
import requests


def count_words(subreddit, word_list, count_list=[], page_2=None):
    if not count_list:
        for word in word_list:
            count_list.append(dict({'keyword': word,
                                   'count': 0}))
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if page_2:
        url += '?after={}'.format(page_2)

    headers = {'User-Agent': 'Shovi'}

    res = resquests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return

    data = res.json()['data']

    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    page_2 = data['after']
    if page_2 is not None:
        return count_words(subreddit, word_list, count_list, page_2)
    else:
        # sort the list by count
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']),
                             reverse=True)
    keywords = 0
    for word in sorted_list:
        if word['count'] > 0:
            print('{}: {}'.format(word['keyword'], word['count]))
            keywords += 1
    return

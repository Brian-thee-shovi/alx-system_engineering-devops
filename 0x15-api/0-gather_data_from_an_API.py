#!/usr/bin/python3
"""
returns info of employees TODO list
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
       userid = sys.argv[1]

       apiurl = 'https://jsonplaceholder.typicode.com/'
       userurl = apiurl + 'users/{}'.format(userid)
       user_todos = apiurl + 'users/{}/todos'.format(userid)

       #requests data
       user = requests.get(userurl).json()
       todos = requests.get(user_todos).json()

       titles = [todo.get('title') for todo in todos if todo.get('completed')]

       print("Employee {} is done with tasks({}/{}):".format(
           user.get('name'), len(titles), len(todos)))
       print('\n'.join(['\t {}'.format(title) for title in titles]))



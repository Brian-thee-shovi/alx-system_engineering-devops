#!/usr/bin/python3
"""
exports a user TODO list as a CSV file
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        userid = sys.argv[1]

        apiurl = 'https://jsonplaceholder.typicode.com/'
        userurl = apiurl + 'user/{}'.format(userid)
        user_todos = apiurl + 'users/{}/todos'.format(userid)

        # requests data
        user = requests.get(userurl).json()
        todos = requests.get(user_todos).json()

        csv_data = ['"{}","{}","{}","{}"'.format(
            userid,
            user.get('username'),
            todo.get('completed'),
            todo.get('title')) for todo in todos]

        with open('{}.csv'.format(userid), 'w') as csvf:
            csvf.write('\n'.join(csv_data))

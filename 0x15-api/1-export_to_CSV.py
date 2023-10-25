#!/usr/bin/python3
"""
exports a user TODO list as a CSV file
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]

        apiurl = 'https://jsonplaceholder.typicode.com/'
        userurl = apiurl + 'user/{}'.format(user_id)
        user_todos = apiurl + 'users/{}/todos'.format(user_id)

        # requests data
        user = requests.get(userurl).json()
        todos = requests.get(user_todos).json()

        csv_data = ['"{}","{}","{}","{}"'.format(
            user_id,
            user.get('username'),
            todo.get('completed'),
            todo.get('title')) for todo in todos]

        with open('{}.csv'.format(user_id), 'w') as csvf:
            csvf.write('\n'.join(csv_data))

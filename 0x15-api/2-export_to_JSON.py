#!/usr/bin/python3
"""
converts user TODO list as to json data
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        userid = sys.argv[1]

        apiurl = 'https://jsonplaceholder.typicode.com/'
        userurl = apiurl + 'users/{}'.format(userid)
        user_todos = apiurl + 'users/{}/todos'.format(userid)

        # request data
        user = requests.get(userurl).json()
        todos = requests.get(user_todos).json()

        json_data = [
                {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user.get('username')
                }
                for todo in todos]
        with open('{}.json'.format(userid), 'w') as jsonf:
            json.dump({userid: json_data}, jsonf)

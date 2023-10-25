#!/usr/bin/python3
"""
exports all todos as json files
"""
import json
import requests
import sys

# endpoint urls
apiurl = 'https://jsonplaceholder.typicode.com/'
usersurl = apiurl + 'users'
todosurl = apiurl + 'todos'


if __name__ == "__main__":

    # requests user data
    users = requests.get(usersurl).json()

    with open("todo_all_employees.json", 'w') as jsonf:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(todosurl,
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonf)

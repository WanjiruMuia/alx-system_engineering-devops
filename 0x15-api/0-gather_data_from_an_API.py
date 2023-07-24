#!/usr/bin/python3
"""Script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests as r

if __name__ == '__main__':
    employee_id = 2  # Employee ID for Ervin Howell
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = r.get(url + 'users/{}'.format(employee_id)).json()
    to_do = r.get(url + 'todos', params={'userId': employee_id}).json()
    completed = [title.get("title") for title in to_do if title.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"), len(completed), len(to_do)))
    [print("\t {}".format(title)) for title in completed]

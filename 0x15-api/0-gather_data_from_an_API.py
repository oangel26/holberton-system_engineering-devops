#!/usr/bin/python3
"""
Python script that using REST API, for a given given employee ID, returns \
information about his/her TODO list progress.
"""


from urllib import request
from sys import argv
import json


with request.urlopen('https://jsonplaceholder.typicode.com/users/' +
                     argv[1]) as response:
    employee_json = response.read()


with request.urlopen('https://jsonplaceholder.typicode.com/users/' +
                     argv[1] + '/todos') as response:
    employee_todos_json = response.read()

employee_todos_list = json.loads(employee_todos_json)
employee_dict = json.loads(employee_json)


count = 0
for employee_todos_dict in employee_todos_list:
    if employee_todos_dict["completed"] is True:
        count += 1


print("Employee {} is done with tasks({}/{}):".
      format(employee_dict["name"], count, len(employee_todos_list)))
for employee_todos_dict in employee_todos_list:
    if employee_todos_dict["completed"] is True:
        print('\t ' + employee_todos_dict["title"])

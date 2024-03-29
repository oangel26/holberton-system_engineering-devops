#!/usr/bin/python3
"""
Python script that using REST API, for a given given employee ID, returns
information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        print("USAGE: python3 [MODULE NAME] [EMPLOYEE ID]")
    else:
        response = requests.get('https://jsonplaceholder.typicode.com/users/' +
                                sys.argv[1])
        employee_dict = response.json()

        response = requests.get('https://jsonplaceholder.typicode.com/users/' +
                                sys.argv[1] + '/todos')
        employee_todos_list = response.json()

        count = 0
        for employee_todos_dict in employee_todos_list:
            if employee_todos_dict["completed"] is True:
                count += 1

        print("Employee {} is done with tasks({}/{}):".
              format(employee_dict["name"], count, len(employee_todos_list)))
        for employee_todos_dict in employee_todos_list:
            if employee_todos_dict["completed"] is True:
                print('\t ' + employee_todos_dict["title"])

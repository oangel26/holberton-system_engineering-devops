#!/usr/bin/python3
"""
Python script that using REST API, for a given given employee ID, returns
information about his/her TODO list progress, exporting data in JSON format.
"""


if __name__ == "__main__":
    import json
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

        employee_records = {}
        employee_new_list = []
        for i in employee_todos_list:
            employee_new_todos = {}
            employee_new_todos["task"] = i["title"]
            employee_new_todos["completed"] = i["completed"]
            employee_new_todos["username"] = employee_dict["username"]
            employee_new_list.append(employee_new_todos)

        employee_records[employee_dict["id"]] = employee_new_list

        with open(sys.argv[1] + '.json', 'w', encoding='utf-8') as f:
            json.dump(employee_records, f)

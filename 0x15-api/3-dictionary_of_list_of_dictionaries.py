#!/usr/bin/python3
"""
Python script that using REST API, for a given given employee ID, returns
information about his/her TODO list progress, exporting data in JSON format.
"""


if __name__ == "__main__":
    import json
    import requests

    response = requests.get('https://jsonplaceholder.typicode.com/users')
    employee_list_info = response.json()

    employees_records = {}
    for employee_dict in employee_list_info:
        response = requests.get('https://jsonplaceholder.typicode.com/users/' +
                                str(employee_dict["id"]) + '/todos')
        employee_todos_list = response.json()
        employee_new_list = []
        for i in employee_todos_list:
            employee_new_todos = {}
            employee_new_todos["task"] = i["title"]
            employee_new_todos["completed"] = i["completed"]
            employee_new_todos["username"] = employee_dict["username"]
            employee_new_list.append(employee_new_todos)

        employees_records[employee_dict["id"]] = employee_new_list

    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(employees_records, f)

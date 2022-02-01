#!/usr/bin/python3
"""
Python script that using REST API, for a given given employee ID, returns
information about his/her TODO list progress in a CSV file.
"""


if __name__ == "__main__":
    import csv
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

        with open(sys.argv[1] + '.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for i_dict in employee_todos_list:
                csv_list = []
                csv_list.append(i_dict["userId"])
                csv_list.append(employee_dict["username"])
                csv_list.append(i_dict["completed"])
                csv_list.append(i_dict["title"])
                writer.writerow(csv_list)

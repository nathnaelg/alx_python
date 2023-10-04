#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
import requests
import sys


def export_to_CSV(user_id):
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()["name"]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    ).json()

    tasks_data = []

    for task in tasks:
        tasks_data.append(
            [
                str(user_id),
                employee_name,
                task["completed"],
                task["title"],
            ]
        )

    with open(str(user_id) + ".csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(tasks_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_CSV(employee_id)
    except ValueError:
        print("Please provide a valid employee ID.")

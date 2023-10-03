#!/usr/bin/python3
import csv
import requests
import sys


def export_to_CSV(employee_id):
    # The API requests and data extraction will remain the same as in the provided script.

    # Get employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["username"]

    # Get TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create or overwrite the CSV file
    with open(f"{employee_id}.csv", "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name,
                            task["completed"], task["title"]])

    print(f"Data exported to {employee_id}.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_CSV(employee_id)
    except ValueError:
        print("Please provide a valid employee ID.")

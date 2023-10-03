"""Accessing a REST API for todo lists of employees"""
import json
import requests
import sys


def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        return

    user_id = employee_data["id"]
    username = employee_data["username"]

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return

    # Create a dictionary to store tasks
    tasks_dict = {user_id: []}

    for task in todos_data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        tasks_dict[user_id].append(task_dict)

    # Export data to JSON file
    json_file_name = f"{user_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(tasks_dict, json_file, indent=4)

    print(f"Data exported to {json_file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_info(employee_id)

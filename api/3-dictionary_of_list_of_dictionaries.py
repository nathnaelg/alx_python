"""Accessing a REST API for todo lists of employees"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    username = user_data["username"]

    # Fetch tasks data for the given user
    tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks_data = tasks_response.json()

    # Create a dictionary to store tasks for all users
    all_tasks = {}

    # Iterate through tasks to organize them by user
    for task in tasks_data:
        user_id = task["userId"]
        if user_id not in all_tasks:
            all_tasks[user_id] = []

        task_data = {
            "username": username,
            "task": task["title"],
            "completed": task["completed"],
        }

        all_tasks[user_id].append(task_data)

    # Export the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)

print('User ID and Tasks output: OK')

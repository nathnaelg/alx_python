#!/usr/bin/python3
"""
Exporitng the data from the api requests to csv file
"""
import csv
import requests
import sys

if __name__=="__main__":
    user_id = sys.argv[1]

    # getting user
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url)
    user_data = user.json()

    # getting todos
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    todos = requests.get(todo_url)
    todos_data = todos.json()

    # exporting the data to csv
    csv_file = "{}.csv".format(user_id)

    with open(csv_file, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for task in todos_data:
            csv_writer.writerow([user_id, user_data['name'], task['completed'],task['title']])

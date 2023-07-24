#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee information
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()

        # Fetch employee's TODO list
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        # Display progress
        print(f"Employee {employee_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo['completed']:
                print("\t", todo['title'])

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

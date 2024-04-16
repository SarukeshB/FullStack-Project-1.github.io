import argparse
import requests

BASE_URL = 'http://localhost:8000/' 


def list_tasks():
    response = requests.get(BASE_URL + 'get-data/')
    if response.status_code == 200:
        tasks = response.json()
        for task in tasks:
            print(task)
    else:
        print('Failed to retrieve tasks')


def add_task(id, title, due_date):
    data = {'id':id ,'title': title, 'due_date': due_date}
    response = requests.post(BASE_URL + 'store-name/', json=data)
    if response.status_code == 200:
        print('Task added successfully')
    else:
        print('Failed to add task')


def delete_task(task_id):
    data = {'id': task_id}
    response = requests.post(BASE_URL + 'delete-data/', json=data)
    if response.status_code == 200:
        print(f'Task {task_id} deleted successfully')
    else:
        print(f'Failed to delete task {task_id}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['list', 'add', 'delete'], help='Action to perform')
    parser.add_argument('--title', help='Title of the task')
    parser.add_argument('--due_date', help='Due date of the task')
    parser.add_argument('--id', help='ID of the task to delete')

    args = parser.parse_args()

    if args.action == 'list':
        list_tasks()
    elif args.action == 'add':
        if not args.title or not args.due_date:
            parser.error('something is missing bro')
        add_task(args.id ,args.title, args.due_date)
    elif args.action == 'delete':
        if not args.id:
            parser.error('--id is required for action "delete"')
        delete_task(args.id)


if __name__ == '__main__':
    main()

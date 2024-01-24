import datetime

to_do_list = []


def add_task():
    title = input("Enter task title: ")
    description = input("Enter description of the task")
    due_date = input("Enter due date in formate DD-MM-YYYY")

    try:
        due_date = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return
    task = {"task": title, "description": description, "due_date": due_date}
    to_do_list.append(task)
    print("task added successfully")


def view_task():

    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}. Title: {task.get('task', 'No Title')}")
        print(f"   Description: {task.get('description', 'No Description')}")
        due_date = task.get('due_date')
        print(f"   Due Date: {due_date.strftime('%d-%m-%Y')}")


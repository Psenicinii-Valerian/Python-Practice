# add task, complete task, filter, task_to_string
# filter, map
import sys

tasks = []
index = 1


def add_task(name, status):
    global index
    task = {
        "index": index,
        "name": name,
        "status": status
    }
    tasks.append(task)
    index += 1


def complete_task(index):
    for task in tasks:
        if task['index'] == index:
            task['status'] = "complete"


def filter_by_status(task, status):
    return task['status'] == status


def task_to_string(task):
    return f"{task['index']}. {task['name']}: {task['status']}"


def menu():
    while(True):
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. Filter tasks by status")
        print("4. Show all tasks")
        print("5. Exit app")
        choice = int(input("Enter your choice: "))
        print()
        match(choice):
            case 1:
                name = input("Enter task's name: ")
                status = input("Enter task's status(complete/incomplete): ")
                add_task(name, status)
            case 2:
                index = int(input("Enter the index of the task you want to mark as completed: "))
                complete_task(index)
            case 3:
                status = input("Enter the status of the tasks you want to see(complete/incompete): ")
                status_filter = list(filter(lambda task: filter_by_status(task, status), tasks))
                if len(status_filter) == 0:
                    print(f"There are not any tasks that have the status: {status}")
                else:
                    print(f"Tasks with the status: {status}:")
                    for task in status_filter:
                        print(task_to_string(task))
            case 4:
                if len(tasks) == 0:
                    print(f"There are not any created tasks yet. Add some!")
                else:
                    print("All tasks:")
                    for task in tasks:
                        print(task_to_string(task))
            case 5:
                sys.exit(0)
            case _:
                print("Invalid option!")
        print()


# calling the menu method
if __name__ == "__main__":
    menu()

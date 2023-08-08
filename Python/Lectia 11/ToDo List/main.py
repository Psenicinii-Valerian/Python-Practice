class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    # __str__ - ne permite sa printam la ecran obiectul nostru sub forma de string (un fel de metoda toString())
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name}\nDescription: {self.description}\nStatus: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.mark_as_completed()
            print("Task marked as completed")
        else:
            print("Invalid task index")

    def display_tasks(self):
        if self.tasks:
            # enumerate - metoda ce numara pozitia fiecarui element dintr-o colectie
            for index, task in enumerate(self.tasks):
                print(f"Task {index+1}")
                print(task)
        else:
            print("No tasks found")

    def delete_task(self, task_index):
        if task_index < len(self.tasks):
            # del - operator ce sterge orice(colectie/variabila/orice alt ceva)
            del self.tasks[task_index]
            print("Task deleted")
        else:
            print("Invalid task index")


def main():
    todo_list = ToDoList()
    while True:
        print("=========== ToDo Menu ===========")
        print("1. Add Task")
        print("2. Mark Task as completed")
        print("3. Display Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # switch case in Python
        match choice:
            case "1":
                name = input("Enter Task Name: ")
                description = input("Enter Task Description: ")
                todo_list.add_task(name, description)
                print("Task added successfully.\n")
            case "2":
                task_index = int(input("Enter task index to mark as completed: "))
                todo_list.mark_task_completed(task_index - 1)
                print()
            case "3":
                print("Current Tasks: ")
                todo_list.display_tasks()
                print()
            case "4":
                task_index = int(input("Enter task index to delete: "))
                todo_list.delete_task(task_index - 1)
                print()
            case "5":
                print("Thank you for using my program!")
                break
                # SystemExit()
            case _:
                print("Invalid menu choice.\n")

if __name__ == "__main__":
    main()

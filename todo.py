from rich import print
from rich.table import Table
import datetime
import json



class Uppgift:
    def __init__(self, title, description, due_date, prioritet):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.prioritet= prioritet

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {self.prioritet} - {status} (Due: {self.due_date})"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def list_tasks(self):
        table = Table(title="Mina uppgifter")
        table.add_column("Titel", style="cyan")
        table.add_column("Prioritet", style="magenta")
        table.add_column("Status", style="green")
        table.add_column("Datum", style="yellow")
        for task in self.tasks:
            status = "✓ Klar" if task.completed else "○ Pending"
            table.add_row(task.title, task.prioritet, status, task.due_date)
        print(table)

    def mark_task_as_completed(self, task):
        task.mark_as_completed()

    def save_to_file(self, filename):
        data = []
        for task in self.tasks:
            data.append({
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "completed": task.completed
            })
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            for task_data in data:
                task = Uppgift(
                    task_data["title"],
                    task_data["description"],
                    task_data["due_date"],
                    task_data.get("prioritet", "medel")
                )
                task.completed = task_data["completed"]
                self.tasks.append(task)
        except FileNotFoundError:
            print("Ingen sparad lista hittades. Startar med tom lista.")

    def filter_tasks(self, status):
        if status == "completed":
            return [task for task in self.tasks if task.completed]
        elif status == "pending":
            return [task for task in self.tasks if not task.completed]
        else:
            return self.tasks

    def statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task.completed])
        pending_tasks = total_tasks - completed_tasks
        return {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks
        }
todo=TodoList()
todo.load_from_file("tasks.json")
while True:
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Mark Task as Completed")
    print("5. Filter Tasks")
    print("6. Show Statistics")
    print("7. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        prioritet = input("Prioritet (hög/medel/låg): ")
        task = Uppgift(title, description, due_date, prioritet)
        todo.add_task(task)
        print("Task added successfully.")

    elif choice == "2":
        title = input("Enter the title of the task to remove: ")
        task_to_remove = next((task for task in todo.tasks if task.title == title), None)
        if task_to_remove:
            todo.remove_task(task_to_remove)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    elif choice == "3":
        todo.list_tasks()

    elif choice == "4":
        title = input("Enter the title of the task to mark as completed: ")
        task_to_complete = next((task for task in todo.tasks if task.title == title), None)
        if task_to_complete:
            todo.mark_task_as_completed(task_to_complete)
            print("Task marked as completed.")
        else:
            print("Task not found.")

    elif choice == "5":
        status = input("Filter by status (completed/pending): ").lower()
        filtered_tasks = todo.filter_tasks(status)
        for task in filtered_tasks:
            print(task)

    elif choice == "6":
        stats = todo.statistics()
        print(f"Total tasks: {stats['total']}")
        print(f"Completed tasks: {stats['completed']}")
        print(f"Pending tasks: {stats['pending']}")

    elif choice == "7":
        todo.save_to_file("tasks.json")
        print("Tasks saved. Exiting...")
        break

    else:
        print("Invalid option. Please try again.")   
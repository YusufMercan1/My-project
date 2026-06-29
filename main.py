from rich import print
from rich.table import Table
from models import Uppgift
from storage import spara, ladda

todo_tasks = ladda("tasks.json")

while True:
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Mark Task as Completed")
    print("5. Show Statistics")
    print("6. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        prioritet = input("Prioritet (hög/medel/låg): ")
        task = Uppgift(title, description, due_date, prioritet)
        todo_tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        title = input("Enter the title of the task to remove: ")
        task_to_remove = next((t for t in todo_tasks if t.title == title), None)
        if task_to_remove:
            todo_tasks.remove(task_to_remove)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    elif choice == "3":
        table = Table(title="Mina uppgifter")
        table.add_column("Titel", style="cyan")
        table.add_column("Prioritet", style="magenta")
        table.add_column("Status", style="green")
        table.add_column("Datum", style="yellow")
        for task in todo_tasks:
            status = "✓ Klar" if task.completed else "○ Pending"
            table.add_row(task.title, task.prioritet, status, task.due_date)
        print(table)

    elif choice == "4":
        title = input("Enter the title of the task to mark as completed: ")
        task_to_complete = next((t for t in todo_tasks if t.title == title), None)
        if task_to_complete:
            task_to_complete.mark_as_completed()
            print("Task marked as completed.")
        else:
            print("Task not found.")

    elif choice == "5":
        total = len(todo_tasks)
        completed = len([t for t in todo_tasks if t.completed])
        pending = total - completed
        print(f"Total: {total}, Klara: {completed}, Kvar: {pending}")

    elif choice == "6":
        spara("tasks.json", todo_tasks)
        print("Tasks saved. Exiting...")
        break

    else:
        print("Invalid option. Please try again.")
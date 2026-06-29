import json
from models import Uppgift

def spara(filename, tasks):
    data = []
    for task in tasks:
        data.append({
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "completed": task.completed,
            "prioritet": task.prioritet
        })
    with open(filename, 'w') as file:
        json.dump(data, file)

def ladda(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        tasks = []
        for task_data in data:
            task = Uppgift(
                task_data["title"],
                task_data["description"],
                task_data["due_date"],
                task_data.get("prioritet", "medel")
            )
            task.completed = task_data["completed"]
            tasks.append(task)
        return tasks
    except FileNotFoundError:
        return []
class Uppgift:
    def __init__(self, title, description, due_date, prioritet):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.prioritet = prioritet

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {self.prioritet} - {status} (Due: {self.due_date})"
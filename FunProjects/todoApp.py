class TodoList:
    def __init__(self):
        self.tasks = set()

    def add_task(self, task):
        self.tasks.add(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print("The task was not found")
    def display_tasks(self):
        for task in self.tasks:
            print(f"- {task}")

 
todo = TodoList()
todo.add_task("Complete Python project")
todo.add_task("Read a book")
todo.display_tasks()
todo.remove_task("Exercise")  

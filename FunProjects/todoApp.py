class TodoList:
    def __init__(self):
        self.tasks = set()

    def add_task(self, task):
        self.tasks.add(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
 
        if r in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print("Couldn't find the task")
 
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
 
            print("The task was not found")
 
            print(f"task'{task}'not found in the list")
 

 
    def display_tasks(self):
        if self.tasks:
            print("your task:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("no task in the list")

 
todo = TodoList()
n=int(input("Enter no. of tasks to add:"))
for i in range(n):
    t=input("Enter the task to add:")
    todo.add_task(t)
todo.display_tasks()
r=input("Enter a task to remove:")
todo.remove_task(r)



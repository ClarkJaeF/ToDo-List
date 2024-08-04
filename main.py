print("ToDo List")

class Task:
    def __init__(self, name, status="Incomplete"):
        self.name = name
        self.status = status

    def mark_completed(self):
        self.status = "Completed"

    def mark_incomplete(self):
        self.status = "Incomplete"

class TaskList:
    def __init__(self, name, tags=None):
        if tags is None:
            tags = []
        self.name = name
        self.tags = tags
        self.tasks = []

    def add_tags(self, new_tag):
        if new_tag not in self.tags:
            self.tags.append(new_tag)

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def display_tasks(self):
        print(f"Tasks in '{self.name}':")
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(f" - {task.name}: {task.status}")

class TaskManager:
    @staticmethod
    def add_task(task_list, task_name):
        task = Task(task_name)
        task_list.add_task(task)

    @staticmethod
    def remove_task(task_list, task_name):
        task_list.remove_task(task_name)

    @staticmethod
    def mark_task_completed(task_list, task_name):
        task = next((t for t in task_list.tasks if t.name == task_name), None)
        if task:
            task.mark_completed()
        else:
            print("Task not found")

    @staticmethod
    def mark_task_incomplete(task_list, task_name):
        task = next((t for t in task_list.tasks if t.name == task_name), None)
        if task:
            task.mark_incomplete()
        else:
            print("Task not found")

    @staticmethod
    def display_tasks(task_list):
        task_list.display_tasks()

class ListManager:
    def __init__(self):
        self.lists = {}

    def create_list(self):
        list_name = input("Enter the name of the list: ")
        tags = input("Enter tags for the list, separated by commas: ").split(",")
        self.lists[list_name] = TaskList(list_name, [tag.strip() for tag in tags])
    
    def remove_list(self, list_name):
        if list_name in self.lists:
            self.lists.pop(list_name)
            print(f"List '{list_name}' removed.")
        else:
            print("List not found")

    def get_task_list(self, list_name):
        return self.lists.get(list_name, None)

    def display_list(self, list_name):
        task_list = self.get_task_list(list_name)
        if task_list:
            TaskManager.display_tasks(task_list)
        else:
            print("List not found")

if __name__ == "__main__":
    manager = ListManager()
    
    actions = {
        "1": manager.handle_create_list,
        "2": manager.handle_remove_list,
        "3": manager.handle_add_task,
        "4": manager.handle_remove_task,
        "5": manager.handle_mark_task_completed,
        "6": manager.handle_mark_task_incomplete,
        "7": manager.handle_display_list
    }
    
    while True:
        print("\n1. Create a new list")
        print("2. Remove a list")
        print("3. Add a task to a list")
        print("4. Remove a task from a list")
        print("5. Mark a task as completed")
        print("6. Mark a task as incomplete")
        print("7. Display tasks in a list")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "8":
            break
        
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice")
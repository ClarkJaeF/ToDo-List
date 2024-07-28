print("ToDo List")

class TaskList:
    def __init__(self, name, tags = None):
        if tags is None:
            tags = []
        self.name = name
        self.tags = tags
        self.listOfTasks = []

    def add_tags(self, new_tag):
        self.tags.append(new_tag)

    def add_task(self, new_task):
        self.listOfTasks.append(new_task)
    
class Task:
    def __init__(self, name, status="Incomplete"): 
        self.name = name 
        self.status = status
         
    def mark_completed(self): 
        self.status = "Completed"

    def mark_incomplete(self): 
        self.status = "Incomplete"

class ListManager:
    def __init__(self):
        self.lists = {}
    
    def create_list(self):
        list_name = input("Enter the name of the list: ")
        self.lists[list_name] = TaskList(list_name)
    
    def remove_list(self, list_name):
        if list_name in self.lists:
            self.lists.pop(list_name)
        else:
            print("List not found")
    
    def display_list(self, list_name):
        pass
       
def display_list_options():
    print("1. Select a list")
    print("2. Add a list")
    print("3. Delete a list")
    
def display_task_options():
    print("1. Add tag to list")
    print("2. Mark completed")
    print("3. Mark incomplete")
    print("4. Add a Task")
    print("5. Remove a Task")



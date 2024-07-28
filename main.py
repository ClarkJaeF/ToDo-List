print("ToDo List")

class List: 
    def __init__(self, name, tags = []):
        self.name = name 
        self.tags = tags
        self.listOfTasks = []

    def addTags(self, newTag):
        self.tags.append(newTag)

    def addTasks(self, newTask):
        self.tags.append(newTask)

def createList():
    listName = str(input())
    listName = List(listName)
    

class Task:
    def __init__(self, name, status = "Incomplete"): 
         self.name = name 
         self.status = status
         
    def markCompleted(self): 
         self.stauts = "Completed"

    def markIncompleted(self): 
         self.stauts = "Incomplete"

def displayOptions(): 
    pass 

def addTasks():
    pass

def removeTasks(): 
    pass 


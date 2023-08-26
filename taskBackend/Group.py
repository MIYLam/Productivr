from Task import Task

class Group:
    tasks = []
    groupMembers = []
    
    def __init__(self, name):
        self.name = name
    
    def addTask(self, task: Task):
        self.tasks.append(task)
        
    def addMembers(self, user_id):
        self.groupMembers.append(user_id)
        
        
    def getMembers(self):
        for user in self.groupMembers:
            print(user)
    

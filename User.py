from Task import Task
from Group import Group
from random import randint
class User:
    tasks = []
    groups = []
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.groups = []  # List of group IDs or Group objects

    
    def createTask(self, description, title, group):
        task = Task(title, description, self , group )
        self.tasks.append(task)
        group.addTask(task)
    
    def createGroup(self,name):
        group = Group(name)
        self.groups.append(group)
        group.addMembers(self)
        
    def joinGroup(self, group):
        self.groups.append(group)
        group.addMember(self)
        
    def addToTasks(self, task: Task):
        self.tasks.append(task)
    

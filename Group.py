from Task import Task
from typing import List

class Group:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []  # List of task IDs or Task objects
    
    def addTask(self, task: Task):
        self.tasks.append(task)
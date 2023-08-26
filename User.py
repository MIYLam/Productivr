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

    def create_task(self, description, title, group):
        task = Task(title, description, self, group)
        self.tasks.append(task)
        group.add_task(task)

    def create_group(self, name):
        group = Group(name)
        self.groups.append(group)
        group.add_members(self)

    def join_group(self, group):
        self.groups.append(group)
        group.add_member(self)

    def add_to_tasks(self, task: Task):
        self.tasks.append(task)

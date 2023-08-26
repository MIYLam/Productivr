from Task import Task


class Group:
    tasks = []
    group_members = []

    def __init__(self, name):
        self.name = name

    def add_task(self, task: Task):
        self.tasks.append(task)

    def add_members(self, user_id):
        self.group_members.append(user_id)

    def get_members(self):
        for user in self.group_members:
            print(user)

    def get_group_tasks(self):
        for task in self.tasks:
            print(task)

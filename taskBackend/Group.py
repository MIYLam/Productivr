class Group:
    def __init__(self, name):
        self.name = name
        self.tasks = []  # List of task IDs or Task objects

    def add_task(self, task: Task):
        self.tasks.append(task)

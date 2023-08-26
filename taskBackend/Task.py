class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

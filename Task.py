class Task:
    
    def __init__(self, title, description, user_id, group_id):
        self.title = title
        self.description = description
        self.is_completed = False
        self.user = user_id
        self.group = group_id
    
    def mark_as_completed(self):
        self.is_completed = True

class Task:
    def __init__(self, title, description, user_id, group_id):
        self.title = title
        self.description = description
        self.is_completed = False
        self.user = user_id
        self.group = group_id
        self.task_ID = self.generate_ID()
        self.update_database()

    def update_database(self):
        """
        put the data into database
        """
        pass

    def generate_ID(self):
        """
        Pull from database, and count number of rows + 1 and assign it as the ID
        """
        return 1

    def mark_as_completed(self):
        self.is_completed = True

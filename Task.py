class Task:  
    def __init__(self, title, description, user_id, group_id):
        self.title = title
        self.description = description
        self.is_completed = False
        self.user = user_id
        self.group = group_id
        self.taskID = self.generateID()
        self.updateDatabase()
    
    def updateDatabase(self):
        """
        put the data into database
        """
        pass
    
    def generateID(self):
        """
        Pull from database, and count number of rows + 1 and assign it as the ID
        """
        return 1
    
    def mark_as_completed(self):
        self.is_completed = True

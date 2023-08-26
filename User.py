class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    
    def createTask(self, description, title, group):
        task = Task(title, description, self.username , group )
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
    
    def getGroups(self):
        return self.groups
    
    def getTasks(self):
        return self.tasks
    

    def add_group(self, group):
        self.groups.append(group)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.groups = []  # List of group IDs or Group objects

    def add_group(self, group):
        self.groups.append(group)

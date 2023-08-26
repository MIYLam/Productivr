from Group import Group
from typing import List


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.groups: List[Group] = []  # List of group IDs or Group objects

    def add_group(self, group: Group):
        self.groups.append(group)

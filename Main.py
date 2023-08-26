from Group import Group
from User import User
from Task import Task

user = User("Rueien", "Passowrd")
group = Group('test')
user.create_task("Do laundry", "put all clothes in ,", group)
print(user.username + " " + user.password + ": " + user.tasks[0].description)

group.get_members()

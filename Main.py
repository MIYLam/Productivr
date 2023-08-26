from Group import Group
from User import User
from Task import Task

user = User("Rueien", "Passowrd")
group = Group('test')
user.createTask("Do laundry", "put all clothes in ,", group)
print(user.id)
# print(user.username+ " " + user.password + ": " + user.tasks[0].description)

group.getMembers()
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    if user in group.get_users():
        return "User found"

    for group in group.get_groups():
        if is_user_in_group(user,group):
            return "User found"
    return "User not found"

# Test Case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

user = "user"
sub_child.add_user(user)

child.add_group(sub_child)
parent.add_group(child)

print (is_user_in_group(user,parent))
# Prints : User found

# Test Case 2
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

user = "user"
sub_child.add_user(user)

child.add_group(sub_child)

print (is_user_in_group(user,parent))
# Prints : User not found (user is not present in subchild and any of its groups )

# Test Case 3
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

user = "user"
sub_child.add_user(user)

child.add_group(sub_child)
parent.add_group(child)

print (is_user_in_group(user, child))
# Prints : User found

# Test Case 4
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

user = "user"

child.add_group(sub_child)

print (is_user_in_group(user,sub_child))
# Prints : User not found (user is not present in subchild and any of its groups )

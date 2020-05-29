#!/usr/bin/python

# Understanding Python class

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")

class User:
    pass

user1 = User()          # user1 is an "instance" of user class
                        # user1 is also called an object.
                        # user1 is an object of class User
# Attach data to this object user1
user1.first_name = "Linus"
user1.last_name = "Torvalds"  
"""
Since first name and last name are attached to an object,
we call them a field.
Field: Data attached to an object.
user1 - Object
first_name - variable
Linux - Value
"""

print(user1.first_name)      # Name of the object dot name of the field
print(user1.last_name)

first_name = "Richard"
last_name = "Stallman"

print("Standalone Name:", first_name, last_name)

print("Value Name attached to user1:", user1.first_name, user1.last_name)

# Create another user object - user2
user2 = User()                          # user2 is an object of class User
user2.first_name = "Mark"
user2.last_name = "Watson"
print("An Auther:", user2.first_name, user2.last_name)

user1.age = 35
user2.favourite_book = "Programmare in Linux"

print(user1.age)
print(user2.favourite_book)

print(user2.age)                        # This will through an error which is expected. See the error carefully.

#help(User)
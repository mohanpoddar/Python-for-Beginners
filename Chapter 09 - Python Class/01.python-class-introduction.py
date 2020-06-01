#!/usr/bin/env python

# Understanding Python class

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")

class User:
    pass

# Create an instance of user class
user1 = User()                              # user1 is an "instance" of user class
                                            # user1 is also called an object.
                                            # user1 is an object of class User

# Attach data to this object user1
user1.first_name = "Linus"                  # first_name is a variable in object user1 and it's value is Linus
user1.last_name = "Torvalds"  
"""
Since first name and last name are attached to an object,
we call them a field.
Field: Data attached to an object.
user1 - Object
first_name - variable
Linux - Value
"""

# Access the object
print(user1.first_name)                     # Name of the object dot name of the field
print(user1.last_name)

# Now Create an standalone variable
first_name = "Richard"
last_name = "Stallman"

print("Standalone Name:", first_name, last_name)                            # Not attached to class as it is standalone.

print("Value Name attached to user1:", user1.first_name, user1.last_name)   # Attached to class User 

# Create another user object - user2
user2 = User()                                                              # user2 is an object of class User
user2.first_name = "Mark"
user2.last_name = "Watson"
print("An Auther:", user2.first_name, user2.last_name)

# Add another field to the object
user1.age = 35
user2.favourite_book = "Programmare in Linux"

# Access the attribute created above.
print(user1.age)
print(user2.favourite_book)

print("All good and as expected!")

time.sleep(1)

print("Now you will see an error, but don't worry. Observe the error carefully.... ")
time.sleep(1)

print(user2.age)                                                            # This will through an error which is expected. See the error carefully.

print("Now you will see an error, but don't worry. Observe the error carefully.... ")
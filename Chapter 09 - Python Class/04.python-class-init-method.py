#!/usr/bin/python

# Understanding Python class - class method
# https://www.ics.uci.edu/~pattis/ICS-33/lectures/class.txt
# https://www.youtube.com/watch?v=8O5kX73OkIY

'''
A function inside a class is called a method.
init = initializaion
a.k.a "Constructor"
name of init method = __init__
init method is called eery time you create a new instance of the class.
The first argument to this method is the world itself, which is a reference to the new object that is being created. 
Additional argument can be added after self.
'''

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")
class Staff:
    def __init__(self):
        print("UK Staff Name - Tom, Jerry, Alex")

    def user(self):
        print("India Staff Name - Prabhas")

usr_1 = Staff()

Staff.user(usr_1)       # 2nd way to access usr_1

usr_1.user()            # 1st way to access usr_1

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print("Running programme : Prog. - 02")
class Staff:
    def __init__(self,name):
        self.name = name
        print("UK Staff Name - Tom, Jerry, Alex")

    def user(self):
        print("India Staff Name is", self.name)

usr_1 = Staff("Prabhas")

Staff.user(usr_1)       # 2nd way to access usr_1

usr_1.user()            # 1st way to access usr_1
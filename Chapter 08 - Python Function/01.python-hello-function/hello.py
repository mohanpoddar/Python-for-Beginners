#!/usr/bin/python

# Understanding Python function and develop a function - hello
# hello function - "hello.py"

def SayHello (name):
    """
    This function greets and encourage person for Python Learning.
    This function should run in the begning of any programme.
    """
    name = input("Write Your Name: ")
    print ("\nHello {}!" " Welocome to Python Learning...".format(name))
    print("Hey", name +  ", Say with me - Python is Awesome..!!")
    return

def SayBye ():
    """
    This function Good Bye to the user.
    This is to run at the end of the programme.
    """
    print("\nGood Bye... \nHappy Learning...\n")
    return

# Call a function
SayHello('name')
SayBye()
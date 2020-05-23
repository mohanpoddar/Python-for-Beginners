#!/usr/bin/python

# Understanding Python function and develop a function - hello
# hello module - "hello.py"

"""
This module for greets and good bye person at begning and the end of the programme.
"""
def SayHello (name):
    """
    This function greets and encourage person for Python Learning.
    This function should run in the begning of any programme.
    """
    name = input("Write Your Name: ")
    print ("\nHello {}!" " Welocome to Python Learning...".format(name))
    print("Hey", name +  ", Say with me - Python is Awesome..!!")

def SayBye ():
    """
    This function Good Bye person.
    This is to run at the end of the programme.
    """
    print("\nGood Bye... \nHappy Learning...\n")
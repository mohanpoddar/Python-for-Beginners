#!/usr/bin/env python

# Understanding user defined function in Python.

import time

print()

#:......................... Function - 01 .........................:
print("Running Function - 01")

def hello():
    name = input("Enter Your Name: ")
    print("Hi", name,", Welcome to Python World..!!!")
    

hello()

print('\n' + "If you see your welcome message then you have successfully created first function in python." + '\n')


#:......................... Function - 02 .........................:
print()
print("Running Function - 02")
time.sleep(1)

def greetings(name):			# Step - 01 : Here name will require an argument
    print("Welcome", name)		# Step - 03 : Takes the value from function argument in step 02

greetings("MyName")			# Step - 02 : MyName value is for argument name


#:......................... Function - 03 .........................:
print()
print("Running Function - 03")
time.sleep(1)

def greetings(name):
    Name = "Python"
    print("Welcome", name)

greetings("MyName")


#:......................... Function - 04 .........................:
print()
print("Running Function - 04")
time.sleep(1)

def greetings(name):			# Step - 01 : Here name will require an argument
    name = "Python"			# Step - 03 : A virable name with value created
    print("Welcome", name)		# Step - 04 : Takes the value from function argument in step 03

greetings("MyName")			# Step - 02 : MyName value is for argument name


#:......................... Function - 05 .........................:
print()
print("Running Function - 05")
time.sleep(1)

def greetings(name):
    print("Welcome", name)
    name = "Python"			# Will not be printed

greetings("MyName")


#:......................... Function - 06 .........................:
print()
print("Running Function - 06")
time.sleep(1)

def AreaOfRectangle(length, breadth):
    area = length * breadth
    return area

A = AreaOfRectangle(5, 6)
print(A)


#:......................... Function - 07 .........................:
print()
print("Running Function - 07")
time.sleep(1)
def first():
    print("Hello first")
    return 5
def second():
    return 20*first()
print (first())
print (second())


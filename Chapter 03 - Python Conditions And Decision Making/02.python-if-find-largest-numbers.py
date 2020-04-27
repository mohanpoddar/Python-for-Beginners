#!/usr/bin/python

# Understanding Python Conditions And Decision Making - if statement
# A programme to find the largest numbers

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
Num1 = int(input("Enter the first number : "))
Num2 = int(input("Enter the second number : "))
Num3 = int(input("Enter the third number : "))

largest = Num1

if Num2 >= largest:
    largest = Num2
if Num3 >= largest:
    largest = Num3
print()
print("The largest number is :", largest, '\n')
if Num1 = Num2 = Num3:    
    print("All three numbers are equal.")

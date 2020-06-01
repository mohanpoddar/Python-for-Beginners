#!/usr/bin/env python

# Understanding use of break statement inside loop

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------: 
print("Running programme : Prog. - 01")
print("Find the Sum of all the positive numbers entered by the user.")

Num = 0
Sum = 0

print ("Enter Numbers to Sum, negative number ends list:")

while True:                     # Will always be true
    Num = eval(input(""))
    if Num < 0:
        break                   # Only way to get out of the loop
    Sum += Num
print("Sum =", Sum)
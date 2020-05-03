#!/usr/bin/python

# Understanding Python loops - for loop

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")
print("Display first 5 even numbers")
time.sleep(1)
EvenNum = [2, 4, 6, 8, 10]
for even in EvenNum: 
    print(even)
print()
time.sleep(1)
#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print("Running programme : Prog. - 02")
print("Display numbers till 10")
time.sleep(1)
for Num in range(0,11):             # range function is zero based
    print(Num)

print()
time.sleep(1)

#:-------------------------------------------- Prog. - 03 --------------------------------------------:
print("Running programme : Prog. - 03")
print ("Display the pattern in gap of 4 starting from 3 till 20.")
time.sleep(1)
for Num in range(3, 20, 4):
    print(Num)
print()
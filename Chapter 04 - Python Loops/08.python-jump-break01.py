#!/usr/bin/env python

# Understanding use of break statement inside loop

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------: 
print("Running programme : Prog. - 01")
for char in "python":
    if char == "h":
        break                               # Will break the loop when char reaches to h
    print (char)
print("The End.")
print()
time.sleep(1)

#:-------------------------------------------- Prog. - 02 --------------------------------------------: 
print("Running programme : Prog. - 02")

Num = 0

for Num in range(20):
    Num = Num + 1
    if Num == 10:
        break                               # Will break the loop when char reaches to h
    print (Num)
print("The End.")
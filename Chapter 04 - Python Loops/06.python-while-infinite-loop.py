#!/usr/bin/env python

# Understanding Python loops - while infinite loop
# 

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01" + '\n')

var = 1
while var == 1:             # Condition resulting in an infinite loop. Press Ctrl + C to terminate.
    Num = int(input("Enter a number: "))
    print("You Entered : ", Num ,  '\n')
print("Good bye")
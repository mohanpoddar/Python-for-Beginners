#!/usr/bin/python

# Understanding Python Conditions And Decision Making - if-else statement

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
Number = int(input("Enter a number:"))
Sqrt = int(Number**0.5)                      # Finding square root of the number.

time.sleep(1)

print()
if Number==Sqrt**2:                          # Verifying if given number is square of it's square root.
   print("This is a square Number!" + "\n" "The square root of",Number, "is :",Sqrt , '\n')   
else:
    print("This is not a square number." + '\n')
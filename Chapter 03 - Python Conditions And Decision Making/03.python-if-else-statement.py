#!/usr/bin/env python

# Understanding Python Conditions And Decision Making - if-else statement

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print()
print("Running programme : Prog. - 01")

x = 15
print("The value of x is",x)

if x > 10:
   print("x is greater than 10")
else:
   print("x is less than 10" )

time.sleep(1)
print()

x = 7
print("The new value of x is",x)

if x > 10:
   print("x is greater than 10")

else:
   print("x is less than 10")

time.sleep(2)

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print()
print("Running programme : Prog. - 02")

Age = 25
if Age >= 18:
   print("If you are", Age, "years old then eligible to caste Vote!" + '\n')           # Printing if statement.
else:
   print("If you are", Age, "years old then not eligible to caste Vote." + '\n')

time.sleep(1)

Age = 12
if Age >= 18:
   print("If you are", Age, "years old then eligible to caste Vote!" + '\n')
else:
   print("If you are", Age, "years old then not eligible to caste Vote." + '\n')       # Printing else statement.

time.sleep(2)

#:-------------------------------------------- Prog. - 03 --------------------------------------------:
print("Running programme : Prog. - 03")
print("Check Your Eligibility to Caste Vote:")
Name = str(input("Enter Your Name: "))
Age = int(input("Enter Your Age: "))

if Age >= 18:
   print('\n' + "Hello", Name, ", you are eligible to caste Vote!" + '\n')
else:
   print('\n' + "Sorry", Name, ", you are not eligible to caste Vote!" + '\n')
time.sleep(1)

#:-------------------------------------------- Prog. - 04 --------------------------------------------:
print()
print("Running programme : Prog. - 04")
print("Check Your Eligibility for Gratuity:")
Name = str(input("Enter Your Name: "))
Syears = int(input("Enter Your Years of Service in Current Job : "))

if Syears >= 5:
   print('\n' + "Congratulations!", Name, ", you are eligible for Gratuity!!" + '\n')
else:
   print('\n' + "Ohh..", Name, "you are not eligible for Gratuity." + '\n')
time.sleep(1)
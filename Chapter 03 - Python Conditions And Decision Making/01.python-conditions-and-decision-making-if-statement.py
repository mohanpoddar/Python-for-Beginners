#!/usr/bin/python

# Understanding Python Conditions And Decision Making - if statement

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print()
print("Running programme : Prog. - 01")

x = 10

if x == 10:
   print("The value of x is: ", x)

time.sleep(1)

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print()
print("Running programme : Prog. - 02")

Age = 18

if Age >= 18:
   print("A person of age 18 or above is eligible to caste Vote!" + '\n')
time.sleep(1)

#:-------------------------------------------- Prog. - 03 --------------------------------------------:
print()
print("Running programme : Prog. - 03")

Age = 15

if Age >= 18:
   print("A person of age 18 or above is eligible to caste Vote!" + '\n')

print("Please Note : A person below of age 18 is not eligible to caste Vote!" + '\n' )
time.sleep(1)

#:-------------------------------------------- Prog. - 04 --------------------------------------------:
print()
print("Running programme : Prog. - 04")
print("Check Your Eligibility to Caste Vote:")
Name = str(input("Enter Your Name: "))
Age = int(input("Enter Your Age: "))

if Age >= 18:
   print('\n' + "Hello", Name, ", You are eligible to caste Vote!" + '\n')

print('\n' + "Please Note: A person of age below 18 is not eligible to caste Vote." + '\n' )
time.sleep(1)

#:-------------------------------------------- Prog. - 05 --------------------------------------------:
print()
print("Running programme : Prog. - 05")
print("Check Your Eligibility for Gratuity:")
Name = str(input("Enter Your Name: "))
Syears = int(input("Enter Your Years of Service in Current Job : "))

if Syears >= 5:
   print('\n' + "Hello", Name, ", You are eligible for Gratuity!" + '\n')

print('\n' + "Please Note: Period of Service below 5 years is not eligible for Gratuity." + '\n' )
time.sleep(1)
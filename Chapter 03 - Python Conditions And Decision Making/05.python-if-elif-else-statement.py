#!/usr/bin/python

# Understanding Python Conditions And Decision Making - if-elif-else statement

# A programme to accept percentage of a student and display grade.

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
#print("Running programme : Prog. - 01")

percentage = float(input("Enter Your Percentage in a Subject: "))
print()

if percentage >= 91 and percentage <=100:
   print("Your Grade : A1")
elif percentage <= 90 and percentage >=81:
   print("Your Grade : A2")
elif percentage <= 80 and percentage >=71:
   print("Your Grade : B1")
elif percentage <= 70 and percentage >=61:
   print("Your Grade : B2")
elif percentage <= 60 and percentage >=51:
   print("Your Grade : C1")
elif percentage <= 50 and percentage >=41:
   print("Your Grade : C2")
elif percentage <= 40 and percentage >=33:
   print("Your Grade : D")
elif percentage > 100:
   print("Invalid Entry. Provide correct value.")
else: 
   print("Needs Improvements.")
print()
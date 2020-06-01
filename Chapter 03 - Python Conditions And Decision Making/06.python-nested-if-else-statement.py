#!/usr/bin/env python

# Understanding Python Conditions And Decision Making - nested-if-else statement

# A programme to decide even and odd numbers.

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("This programme will determine if the number is an even or odd number.")
Num1 = eval(input("Enter A Number: "))

print()

if type(Num1) == float:
   print(Num1, "is not an interger. It's a decimal number. Please enter an integer only:" + '\n')
   Num2 = eval(input("Enter A Number: "))
   if type(Num2) == float:
      print("You have again entered an invalid input, hence existing..." + '\n')
      exit()
   if Num2 >= 0:
      if Num2 % 2 == 0 and Num2 >=1:
         print(Num2, "is a Natural and an Even Number." + '\n')
      if Num2 == 0:
         print(Num2, "is a Whole but an Even Number." + '\n')
      else:
         if Num2 % 2 != 0 and Num2 >=1:
            print(Num2, "is a Natural and an Odd Number." + '\n')
   else: 
      print(Num2, "is a Negative Integer." + '\n')
else:
   if Num1 >= 0:
      if Num1 % 2 == 0 and Num1 >=1:
         print(Num1, "is a Natural and an Even Number." + '\n')
      if Num1 == 0:
         print(Num1, "is a Whole but an Even Number." + '\n')
      else:
         if Num1 % 2 != 0 and Num1 >=1:
            print(Num1, "is a Natural and an Odd Number." + '\n')
   else: 
      print(Num1, "is a Negative Integer." + '\n')
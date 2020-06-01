# Understanding user input in python.

import time

#:........................................ Prog. - 01 ........................................:
print()
print("Running programme : Prog. - 01")
name = str(input('Enter Your Name: '))
age = int(input('Enter Your Age: '))
print('Welcome', name  + '! You are ', age, ' years old.') 

print()

subject = input('Enter Your Favourite Subject: ')
print("You like", subject + " most. Happy Learning..!!!")
print()

print("Remember: The input() function always returns a value of string type and has an issue. See in Prog. - 02" + '\n')
time.sleep(3)

#:........................................ Prog. - 02 ........................................:
print("Running programme : Prog. - 02")
print("Find Sum of two numbers:")
num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")
result = num1 + num2
print("The Sum of", num1, "and", num2, "is: ", result + " (Wrong...)" '\n')

print("why?..." + '\n')
time.sleep(2)

print("Let's check the type of each input numbers and their sum..." + '\n')
time.sleep(2)

print("The Type of Number ", num1, "is: ", type(num1))
time.sleep(1)
print("The Type of Number ", num2, "is: ", type(num2))
time.sleep(1)
print("The Type of Sum", result, "is: ", type(result), '\n')
time.sleep(1)

print("Hope it's clear now and this needs to be fixed. See next programme Prog. - 03" + '\n')

#:........................................ Prog. - 03 ........................................:
print("Running programme : Prog. - 03")
print("Find Sum of two numbers:")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
result = num1 + num2
print("The Sum of", num1, "and", num2, "is: ", result, " (Correct..!!!)"'\n')

print("How?..." + '\n')
time.sleep(2)

print("Let's check the type of each input numbers and their sum..." + '\n')
time.sleep(2)

print("The Type of Number ", num1, "is: ", type(num1))
time.sleep(1)
print("The Type of Number ", num2, "is: ", type(num2))
time.sleep(1)
print("The Type of Sum" , result, "is: ", type(result), '\n')
time.sleep(1)

print("Here input has been modified to integer using another function int()")

print("Hope it's clear now..." + '\n')

#:........................................ Prog. - 04 ........................................:
print(
'''
Instead of modifying the number from string to integer let the programme itself evaluate the value of string. See in Prog. - 04

print Running programme : Prog. - 04

'''
   )
print("Find Sum of two numbers:")
num1 = eval(input("Enter First Number: "))
num2 = eval(input("Enter Second Number: "))
result = num1 + num2
print("The Sum of", num1, "and", num2, "is: ", result, " (Correct..!!!)"'\n')

print("How?..." + '\n')
time.sleep(2)

print("Let's check the type of each input numbers and their sum..." + '\n')
time.sleep(2)

print("The Type of Number ", num1, "is: ", type(num1))
time.sleep(1)
print("The Type of Number ", num2, "is: ", type(num2))
time.sleep(1)
print("The Type of Sum" , result, " is: ", type(result), '\n')
time.sleep(1)

print(
'''
Here input is evaluated to integer using function eval()

Hope it's clear now...

Happy Learning...

'''
    )

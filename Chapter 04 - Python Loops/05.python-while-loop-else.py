#!/usr/bin/env python

# Understanding Python loops - while-else
'''
This programme will find the sum of first n natural numbers. It will display digits one by one in order 
alongwith their sum.
'''

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print('\n' + "Find Sum of First n natural numbers:" + '\n')
time.sleep(0.25)

Num = eval(input("Enter the first n natural numbers for which you want to find Sum, for eg. 10: "))
print(" ")

ordinal = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))


if type(Num) == float or Num <= 0:
   print(Num, "is not a valid input. Please provide valid input:" + '\n')
   Num = eval(input("Enter A Natural Number: "))
   if type(Num) == float or Num <= 0:
      print("You have again entered an invalid input, hence existing..." + '\n')
      exit()

x = 1
Sum = 0

while x < Num + 1:
    print("Display", ordinal(x), "digit     :", x)
    Sum = Sum + x
    print("Sum of First", x, "Digits :", Sum)
    x = x + 1
    print(" ")
    if Num <= 50:
        time.sleep(0.25)
    elif Num > 50 and Num <= 100:
        time.sleep(0.10)
    elif Num > 100 and Num <= 1000:
        time.sleep(0.01)
    elif Num > 1000 and Num <= 10000:
        time.sleep(0.001)
    elif Num > 10000 and Num <= 50000:
        time.sleep(0.0001)   
    else:
        time.sleep(0)
else:
    print("The while loop terminates when value reaches to", x )
    time.sleep(0.5)
    print("The Sum of First", Num, "Digits =", Sum, '\n')

time.sleep(1)
print("What Happend Here?")
time.sleep(1)
print('\n' + "While loop continued until digit achieved maximum value", Num, ", and condition is satified till value", Num, "\nThe loop terminated when value reached to", Num+1, '\n')
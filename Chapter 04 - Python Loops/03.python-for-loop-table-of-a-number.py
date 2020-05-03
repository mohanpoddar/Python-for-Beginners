#!/usr/bin/python

# Understanding Python loops - for loop

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print ('\n' + "Table of 2:" + '\n')
time.sleep(1)

Num = 2
for table in range(1,11):
    print(Num, "x" , table, "=", Num*table)
    time.sleep(0.5)
print()

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print("Now, Tell the number of which table you wish to see...")
time.sleep(1)
Num = eval(input("Enter The Table Number: "))
print()

print("Printing the table of:",Num)

for table in range(1,11):
    print(Num, "x" , table, "=", Num*table)
    time.sleep(0.5)
print()
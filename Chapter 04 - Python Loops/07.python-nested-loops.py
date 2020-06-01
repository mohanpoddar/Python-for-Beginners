#!/usr/bin/env python

# Understanding Python loops - nested loop

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")

i = 2
while (i >= 0):
    print ("Python!", end= " ")
    print ()
    i = i - 1
time.sleep(1)

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print('\n' + "Running programme : Prog. - 02")

i = 2
while (i >= 0):
    j = 2
    while (j >= 0):
        print ("Python!", end=" ")
        j = j - 1
    print ()
    i = i - 1
time.sleep(1)
print('\n' + "Happy Learning!" + '\n')
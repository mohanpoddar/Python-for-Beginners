#!/usr/bin/python

# Understanding Python Dictionary - traversing Dictionary

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
# Method - 01: Using 'in' operator inside for loop
# Traversing or accessing elements of the Dictionary.
print("Running programme : Prog. - 01")
print('\n' + "Display Days of the week:" + '\n')
Day = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

for i in Day:
    print("Day", i, ":" , Day[i])
    time.sleep(0.75)

time.sleep(0.75)
print('\n' + "Happy Learning..!!" + '\n')
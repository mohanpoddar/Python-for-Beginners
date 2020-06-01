#!/usr/bin/env python

# Understanding Python List - list operations 

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print('Lists name of the operations on Lists: ')

ListOperations = ['Concatenation', 'Repetition', 'Membership Testinbg', 'Slicing', 'Indexing']

for i in ListOperations:
    print(" -", i)
    time.sleep(0.25)

print()
time.sleep(0.5)

# Concatenation
print("Running programme : Concatenation")
OSList = ['Linux', 'Solaris']
print("List: ", OSList, "\nAdd AIX to the list")
NewOSList = OSList + ['AIX']
print("NewOSList: ", NewOSList)
print()

# Adding two lists
print("Adding two lists:")
list = ['Learn', 'Python'] + ['Programming']
print(list)

time.sleep(1)
# Repetition
print('\n' + "Running programme : Repetition")
Num = [10,20,30]
print("List: ", Num)
RNum = Num * 2
print("Repeat List: ", RNum)

time.sleep(1)

# Repeat Python 3 times
x = 'Python ' * 3
print(x)
time.sleep(1)

# Membership Testinbg
print('\n' + "Running programme : Membership Testinbg")
device = ('Computer')
print("Device Name: ", device)
print("Verify character u exists: ", 'u' in device)
print("Verify character v exists: ", 'v' in device)
print("Verify character f not exists: ", 'f' not in device)
print("Verify character C not exists: ", 'C' not in device)

time.sleep(1)

# Indexing
print('\n' + "Running programme : Indexing")
OS = ['Linux', 'Solaris', 'AIX']
Num = [5, 10, 15, 20, 25]

print(OS[0])                            # index 0 from begning
print(Num[-1])                          # index from last element

time.sleep(1)

# Slicing
print('\n' + "Running programme : Slicing")
device = 'Computer'
print("Generate All Items: ", device[:])    
print("Generate Items 0 to 3: ", device[:4])
print("Generate Items 1 to 3: ", device[1 : 4 ])
print("Generate Items 1 to 5 with step 2 i.e 1,3,5: ", device[1 : 6 : 2 ])
print("Generate 3rd Items from last: ", device[-3])
print("Generate 3 Items: ", device[-3:])

print()
time.sleep(1)

print("Happy Learning..!!")
print()
time.sleep(1)
#!/usr/bin/env python

# Understanding Python List - traversing list

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
# Method - 01: Using 'in' operator inside for loop
# Traversing or accessing elements of the list.
print("Running programme : Prog. - 01")
table10 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Verify list type:", type(table10))

print("Display list:")
for i in table10:
    print(i)

time.sleep(1)

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
# Method - 02: Using 'range()' function inside for loop
# Traversing or accessing elements of the list.
print()
print("Running programme : Prog. - 02")
vowel = ['a', 'e', 'i', 'o', 'u']
n = len(vowel)                            # len() counts the total number of characters in a string
print("Verify list type:", type(vowel))

print("Display list:")
for i in range(n):
    print(vowel[i])

print("Total number of characters are: ")
print(n)
time.sleep(1)

#:-------------------------------------------- Prog. - 03 --------------------------------------------:
# Method - 02: Using 'range()' function inside for loop
# Traversing or accessing elements of the list.
print()
print("Running programme : Prog. - 03")
vowel = ['a', 'e', 'i', 'o', 'u']
n = len(vowel[1:4])                            # len() counts the total number of characters in a string
print("Verify list type:", type(vowel))

print("Display list:")
for i in range(n):
    print(vowel[i])

print("Total number of characters are: ")
print(n)
print("Happy Learning!!")

subjects = ['Windows', 'Solaris', 'AIX', 'Linux']
temporary = subjects
temporary[0] = 'Android'
print(temporary)
print(subjects)
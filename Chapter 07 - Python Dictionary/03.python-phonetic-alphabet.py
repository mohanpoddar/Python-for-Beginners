#!/usr/bin/env python

# Understanding Python Dictionary - traversing Dictionary to phonetic alphabet

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
# Method - 01: Using 'in' operator inside for loop
# Traversing or accessing elements of the Dictionary.
print("Running programme : Prog. - 01")
print('\n' + "Display NATO Phonetic Alphabet:" + '\n')

Phonetic = {'A':'Alfa', 'B':'Bravo', 'C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'X-ray', 'Y':'Yankee', 'Z':'Zulu'}

for i in Phonetic:
    print(i, ":" , Phonetic[i])
    time.sleep(0.75)
    
time.sleep(0.75)
print('\n' + "Happy Learning..!!" + '\n')
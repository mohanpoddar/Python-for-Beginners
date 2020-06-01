#!/usr/bin/env python

# Understanding Python List - list aliasing 

import time

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")
subjects = ['Windows', 'Solaris', 'AIX', 'Linux']
print(subjects)
print("Creating Alias:")
temporary = subjects                   # Create alias
temporary[0] = 'Android'
print(temporary)
print(subjects)
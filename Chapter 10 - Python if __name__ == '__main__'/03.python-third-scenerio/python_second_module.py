#!/usr/bin/env python

# Python Concepts - if __name__ == '__main__'

import python_first_module

print ("Second Module's Name: {}".format(__name__))

'''
Observe the output carefully. Here, imported module will not give any output as per the condition
in python_first_module, which says to run only when __name__ == '__main__' but this will give
__name__ == python_first_module
'''
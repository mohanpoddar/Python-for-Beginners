#!/usr/bin/env python

# Python Concepts - if __name__ == '__main__'

import python_first_module

print ("Second Module's Name: {}".format(__name__))

'''
Observe the output carefully. Here, imported module will give output as per the condition
in module python_first_module, which says to run when __name__ != '__main__' condition is met.
__name__ == python_first_module
'''
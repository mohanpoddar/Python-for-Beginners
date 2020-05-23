#!/usr/bin/python
"""
A module is a file containing definitions of functions, classes, variables, constants or any other Python objects. 
Contents of this file can be made available to any other program.
"""
# Understanding Python function and develop a function - area
# area module - "area.py"

import math

def rectangle_area (length,breadth):
    return length*breadth

def square_area (side):
    return side*side

def circle_area (radius):
    return math.pi*radius*radius
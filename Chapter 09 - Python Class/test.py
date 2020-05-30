#!/usr/bin/python

class myClass:
    def __init__(self, arg1, arg2):
        self.var1 = arg1
        self.var2 = arg2

    def School(self):
        print(self.var1)
        print(self.var2)

foo = myClass('student', 'teacher')

foo.School()
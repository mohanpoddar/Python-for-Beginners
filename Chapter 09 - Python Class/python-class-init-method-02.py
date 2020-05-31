#!/usr/bin/python

# Understanding Python class - init method
'''
A function inside a class is called a method.
init = initializaion
a.k.a "Constructor"
name of init method = __init__
init method is called eery time you create a new instance of the class.
The first argument to this method is the world itself, which is a reference to the new object that is being created. 
Additional argument can be added after self.
'''
#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")

class Computer:
    def __init__(self,os,ram,disk):
        self.os = os
        self.ram = ram
        self.harddisk = disk                            # See Carefully self.harddisk = disk  

    def config(self):
        print(self)
        print("OS Name: ", self.os)
        print("RAM Amount: ", self.ram)
        print("HardDisk Size: ", self.harddisk)         # See Carefully Variable = harddisk ; Value = disk  

redhat = Computer('rhel7','2GB','500GB')

Computer.config(redhat)
print('---------------------------')
redhat.config()

print()

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print("Running programme : Prog. - 02")
class myClass:
    def __init__(self, arg1, arg2):
        self.var1 = arg1
        self.var2 = arg2

    def School(self):
        print(self.var1)
        print(self.var2)

# Object StTe
StTe = myClass('student', 'teacher')

print(StTe.var2)

# Object TePr
TePr = myClass('teacher', 'principal')

print("Access object StTe:")
StTe.School()

print("Access object TePr:")
myClass.School(TePr)

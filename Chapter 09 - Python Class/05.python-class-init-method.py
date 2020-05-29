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







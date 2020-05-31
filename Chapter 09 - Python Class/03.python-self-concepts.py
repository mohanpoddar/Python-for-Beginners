#!/user/bin/python

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")
def os():
    print("Linux, Solaris, AIX")

os()

#:-------------------------------------------- Prog. - 02 --------------------------------------------:
print("Running programme : Prog. - 02")
def os(self):
    print("Linux, Solaris, AIX")

os("Redhat")


#:-------------------------------------------- Prog. - 03 --------------------------------------------:
print("Running programme : Prog. - 03")

class Employee:

    def details(self):
        print("Name, Age, Email, Pay")

emp_1 = Employee()      # emp_1 is an obeject of Employee class
emp_2 = Employee()

Employee.details(emp_1) # Access object emp_1
Employee.details(emp_2)

emp_1.details()         # Access object emp_1. This will taek emp_1 as a parameter.
emp_2.details()
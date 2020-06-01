#!/usr/bin/env python

# This is a simplified way of doing.

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@email.com"
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}'.format(self.email)

# Add an instance or object
emp_1 = Employee('James', 'Brown', 40000)

emp_2 = Employee(
    'Mike','Posner', 50000
    )

emp_3 = Employee('Test', 'user', 2000,)

# Access the instance 
print(Employee.fullname(emp_1))
print(emp_1.email)
print()

print(emp_2.fullname())
print(Employee.email(emp_2))
print()

print(emp_3.fullname())
print()
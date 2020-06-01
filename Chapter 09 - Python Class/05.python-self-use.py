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

# Add an instance or object
emp_1 = Employee('James', 'Brown', 40000)

emp_2 = Employee(
    'Mike','Posner', 50000
    )

# Access the instance 
print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {}'.format(emp_2.first, emp_2.last))
#!/usr/bin/env python

# This is a simplified way of doing.

#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")
class Employee:

    num_of_emps = 0                                         # Add a Class Variable
    raise_amt = 1.04                                        # Add a Class Variable
    company_name = "MyCompany Pvt. Ltd."                    # Add a Class Variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@email.com"
    
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}'.format(self.email)

    def apply_raise(self):                                  # Add a method to use class variable
        self.pay = int(self.pay * self.raise_amt)

    def company(self):                                      # Add a method company. This will apply globally
        return '{}'.format(self.company_name)

# Add an instance or object
emp_1 = Employee('James', 'Brown', 40000)

emp_2 = Employee(
    'Mike','Posner', 50000
    )

emp_3 = Employee('Test', 'user', 2000)

# Access the instance
print(Employee.fullname(emp_1))
print(emp_1.email)
print()

print(emp_2.fullname())
print(Employee.email(emp_2))
print()

print(emp_3.fullname())
print()

# Access Global Variable - company_name
print("Employee emp_1 Company Name: ", Employee.company(emp_1))
print("Employee emp_2 Company Name: ", Employee.company(emp_2))
print("Employee emp_3 Company Name: ", Employee.company(emp_3))
print()

# Another way to access Global Variable - company_name
print("Employee emp_1 Company Name: ", emp_1.company())
print("Employee emp_2 Company Name: ", emp_2.company())
print("Employee emp_3 Company Name: ", emp_3.company())
print()

# Access Class Variables: num_of_emps
print("Total Number of Employee :", Employee.num_of_emps)
print()

# Access Class Variables: raise_amt
print(Employee.raise_amt)
print(emp_1.raise_amt)
print()

# Apply Raise
print("Before Raise: ", emp_1.pay)                           # Before Raise
emp_1.apply_raise()                                          # Apply raise
print("After Raise: ", emp_1.pay)                            # After Raise
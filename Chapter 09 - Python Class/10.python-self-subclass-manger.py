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

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
# Or        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):                                   # A new subclass Manager

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# Add an instance or object
dev_1 = Developer('James', 'Brown', 40000, 'Python')
dev_2 = Developer('Mike','Posner', 50000, 'Java')

mgr_1 = Manager('Mike', 'Smith', 90000, [dev_1])

# Access Manager Data
print(mgr_1.email)
print()

print('\n' + 'Test1:')
mgr_1.print_emps()              # Print number of employee reporting.

print('\n' + 'Test2:')
mgr_1.add_emp(dev_2)            # Add a new employee         
mgr_1.print_emps()              # Print number of employee reporting.

print('\n' + 'Test3:')
mgr_1.remove_emp(dev_1)         # Remove a new employee
mgr_1.print_emps()              # Print number of employee reporting.

# Some Test
print('\n' + 'Test4:')
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print( '\n' + 'Test5:')
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
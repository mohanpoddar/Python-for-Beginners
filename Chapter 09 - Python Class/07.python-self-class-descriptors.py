#!/user/bin/python

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

# Help on class Employee
print(help(Employee))

# See the descriptors
print(Employee.__dict__)
print()

print(emp_1.__dict__)
print()
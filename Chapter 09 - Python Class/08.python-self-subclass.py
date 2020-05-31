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

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
# Or        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

# Add an instance or object
dev_1 = Developer('James', 'Brown', 40000, 'Python')
dev_2 = Developer('Mike','Posner', 50000, 'Java')

# Access Empoyee
print(dev_1.fullname())
print(dev_1.email)
print(dev_1.pay)
print(dev_1.prog_lang)
print()
#!/usr/bin/python

# Understanding Python class
# https://www.ics.uci.edu/~pattis/ICS-33/lectures/class.txt
# https://www.youtube.com/watch?v=8O5kX73OkIY
#:-------------------------------------------- Prog. - 01 --------------------------------------------:
print("Running programme : Prog. - 01")

class Employee:
    pass

print(Employee)

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

print(type(emp_1))
print(type(emp_2))

# Instance Variabls - Create attribute
emp_1.first = 'James'
emp_1.last = 'Brown'
emp_1.email = 'James.Brown@email.com'
emp_1.pay = '40000'

emp_2.first = 'Mike'
emp_2.last = 'Posner'
emp_2.email = 'Mike.Posner@email.com'
emp_2.pay = '50000'

print(emp_1.email)
print(emp_2.email)

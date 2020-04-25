#!/usr/bin/python

# Understanding Variable Identity in Python
"""
Identity of the Variable:
When a variable in python is assigned a value then it is stored inside a memory location. Hence, it referes address in the memory
which does not change once it has been created. This can be checked using the method id(object) 
"""

>>> x = 5		# Variable x with value 5 is stored inside a memory loction with name x.
>>> x
5
>>> id(x)		# Check memory address of an object.
140412903970624
>>>
>>> y = 10
>>> y
10
>>> id(y)
140412903970784
>>>
>>> z = x+y
>>> z
15
>>> id(z)
140412903970944
>>>
>>> x = 12		
>>> x
12
>>> id(x)		# When value is changed it's id of the variable is also changed.
140412903970848
>>>
>>> y = 14
>>> y
14
>>> id(y)
140412903970912
>>>
>>> z = x+y
>>> z
26
>>> id(z)
140412903971296
>>>
>>> x = 12		
>>> x
12
>>> id(x)		# When same value is re-assigned then id remains unchanged.
140412903970848
>>>
>>> y = 14
>>> y
14
>>> id(y)
140412903970912
>>>
>>> z = x+y
>>> z
26
>>> id(z)
140412903971296
>>>

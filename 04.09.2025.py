'''test_variable = 5/0
print(test_variable, type(test_variable))'''
#1/2 = 0.5 <class 'float'>
#1//2 = 0 <class 'int'>
#10.0//3 = 3.0 <class 'float'>
#10.0/3 = 3.333... <class 'float'>
#15/5.0 = 3.0 <class 'float'>
#15//5.0 = 3.0 <class 'float'>
#5/0 = ZeroDivisionError: division by zero i.e. not possible to complete.
from sys import getsizeof
'''test_var = 12.567
print(test_var, type(test_var), getsizeof(test_var))'''
#string --> "AQA" = AQA <class 'str'> 52
#int --> 1234567890 = 1234567890 <class 'int'> 32
#float --> 12.567 = 12.567 <class 'float'> 24
test_set = set()
test_set.add(1)
print(test_set, type(test_set), getsizeof(test_set))
test_set.add(56)
print(test_set, type(test_set), getsizeof(test_set))
test_set.add(123)
print(test_set, type(test_set), getsizeof(test_set))
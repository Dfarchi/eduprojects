# function as an object

# def foo_power(num1, num2):
#     return num1 ** num2
#
# print(foo_power(3, 4))
#
# print(foo_power)
# #
# my_func_variable = foo_power
# print(my_func_variable)
# #
# # type(foo_power)
# #
# foo_power(4,5)
# print(foo_power.__name__)
# #
# #
# print(my_func_variable(3,4))
# print(foo_power(3,4))



# Now you can pass function as any variable as a param
from typing import Callable


def foo_sum(num1, num2):
    return num1 + num2

def foo_power(num1, num2):
    return num1 ** num2


def operation_on_numbers(op: callable, num1, num2):
    return op(num1, num2)
#
print(operation_on_numbers(foo_sum, 5, 6))
#
print(operation_on_numbers(foo_power, 5, 6))
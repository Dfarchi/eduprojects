from d15.ex1 import single_str_arg
from d15.ex3 import valid_param_types

class Company:
    pass

@single_str_arg
def convert_to_upper(word: str) -> str:
    return word.upper()

@valid_param_types([int, float])
def get_sum(num1, num2):
    return num1 + num2

@valid_param_types([Company])
def my_print(*args):
    print(*args)

# get_sum = valid_param_types([int, float])(get_sum)(4, 5)

if __name__ == '__main__':
    # convert_to_upper(5)
    # convert_to_upper("hello")
    # get_sum(4,5)
    # get_sum("a", "b")

    my_print(Company())

    # valid_param_types([int])(get_sum)(3,4)

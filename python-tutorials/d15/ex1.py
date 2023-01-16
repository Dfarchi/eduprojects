from d15.d15_exceptions import InvalidArgument


def single_str_arg(func):

    def wrapper_func(*args, **kwargs):

        if len(args) != 1 or len(kwargs) != 0 or \
                not isinstance(args[0], str):
            raise InvalidArgument()
        return func(*args, **kwargs)

    return wrapper_func

# @single_str_arg
# def convert_to_upper(word: str) -> str:
#     return word.upper()
#
# convert_to_upper = single_str_arg(convert_to_upper)
#
#
# if __name__ == '__main__':
#     # convert_to_upper(5)
#     convert_to_upper("hello")
#     single_str_arg(convert_to_upper)("hello")
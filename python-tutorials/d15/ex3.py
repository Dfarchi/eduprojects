from d15.d15_exceptions import InvalidArgument


def valid_param_types(valid_types: list):

    def inner(func):

        def wrapper_func(*args, **kwargs):

            for a in args:
                if type(a) not in valid_types:
                    raise InvalidArgument()
            for v in kwargs.values():
                if type(v) not in valid_types:
                    raise InvalidArgument()

            return func(*args, **kwargs)

        return wrapper_func
    return inner


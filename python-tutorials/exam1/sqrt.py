def my_sqrt(x: int) -> int:
    """
    Calculate square root of the number without using built-in
    sqrt operators.
    If the result is float, return the floor value
    :param x:
    :return: the sqrt of the number
    """
    for i in range(0, x+1):
        if i * i == x:
            return i
        elif i * i > x:
            return i-1


if __name__ == '__main__':
    for i in range(11):
        print(f"The sqrt of {i} is {my_sqrt(i)}")

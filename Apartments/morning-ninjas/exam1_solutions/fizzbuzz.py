def fizz_buzz(num: int) -> list[str]:
    """
    Return a list of strings fizz/buzz accorsing to a logic:
    ret_val[i] == "FizzBuzz" if i is divisible by 3 and 5.
    ret_val[i] == "Fizz" if i is divisible by 3.
    ret_val[i] == "Buzz" if i is divisible by 5.
    ret_val[i] == i (as a string) if none of the above conditions are true.
    :param num:
    :return: list with strings
    """
    ret_val: list[str] = []

    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            ret_val.append("FizzBuzz")
        elif i % 3 == 0:
            ret_val.append("Fizz")
        elif i % 5 == 0:
            ret_val.append("Buzz")
        else:
            ret_val.append(str(i))

    return ret_val


if __name__ == '__main__':
    for i in range(0, 20, 3):
        print(f"For i == {i}: {fizz_buzz(i)}")
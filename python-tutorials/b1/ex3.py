def max_of_3(num1: float, num2: float, num3: float) -> float:
    nums_tuple: tuple = (num1, num2, num3)

    # Option I
    # max_num: float = nums_tuple[0]
    # for num in nums_tuple:
    #     if num > max_num:
    #         max_num = num

    # Option II
    max_num = max(nums_tuple)

    return max_num


result = max_of_3(3.9, 43, 1.1)
print(result)

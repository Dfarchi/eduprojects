def second_largest(nums: list[float]) -> float:

    if len(nums) in (0, 1):
        return None

    max_num, second_max = None, None

    for n in nums:
        if max_num is None:
            max_num = n
        else:
            if n > max_num:
                second_max = max_num
                max_num = n
            else:
                if second_max is None:
                    if n != max_num:
                        second_max = n
                else:
                    if second_max < n < max_num:
                        second_max = n

    return second_max
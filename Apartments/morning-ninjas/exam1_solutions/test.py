def second_largest(list1: list) -> int:
    max_num = max(list1[0], list1[1])
    second_max = min(list1[0], list1[1])
    len_n = len(list1)
    for i in range(2, len_n):
        if list1[i] > max_num:
            second_max = max_num
            max_num = list1[i]
        elif second_max < list1[i] and max_num != list1[i]:
            second_max = list1[i]
        elif max_num == second_max and second_max != list1[i]:
            second_max = list1[i]
            print(f"second highest number is: {second_max}")
    return second_max

def fizz_buzz(num: int) -> list:
    ret_val: list = []
    for i in range(num+1):
        if i % 3 == 0 and i % 5 == 0:
            ret_val.append("FizzBuzz")
        elif i % 3 == 0:
            ret_val.append("Fizz")
        elif i % 5 == 0:
            ret_val.append("Buzz")
        else:
            ret_val.append(str(i))
    return ret_val[1::]

if __name__ == '__main__':
    test_lists = (
        [54, -1, 45, 987, 5, 2, 65, 7, 12],
        [3, -4, 2, 3, 0],
        [0, 3, 0],
        [3, 0, 3],
        [3, 3, 3, 3],
        [0, -3, -3, -2, -10],
        [-9, -5, -3, -5, -1],
        [3, 6, 9, 4, 5]
    )
    for nums in test_lists:
        print(f"The second largest of {nums} is {second_largest(nums)}")

    # for i in range(0, 20, 3):
    #     print(f"For i == {i}: {fizz_buzz(i)}")
# Write a number that receives a list of numbers, and finds the second-largest number

# nums = [56, 3, 23, 1, 0, 45, -1, 4, 2, 0] # 45
# nums = [45, 3, 23, 1, 0, 45, -1, 4, 2, 0] # 45
nums = [3, -9, -15, -8, -3] # -3

# option 1

if len(nums) < 2:
    print("Less than 2 elements in list")
    exit(1)

# we have at least 2 elements

if nums[0] < nums[1]:
    max_num = nums[1]
    second_max = nums[0]
else:
    max_num = nums[0]
    second_max = nums[1]

for n in nums[2:]:
    if n < second_max:
        pass
    elif second_max < n <= max_num:
        second_max = n
    else:
        # n > max_num
        # note: the order of commands matters!
        second_max = max_num
        max_num = n

print(second_max)


# option 2 (with None)
# max_num = None
# second_max = None
#
# for n in nums:
#     if max_num is None:
#         max_num = n
#     else:
#         if n > max_num:
#             second_max = max_num
#             max_num = n
#         else:
#             if second_max is None:
#                 second_max = n
#             else:
#                 if second_max < n <= max_num:
#                     second_max = n
#
# print(second_max)
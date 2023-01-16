# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.

import time
import random


def two_sum_inefficient(nums: list[int], target: int) -> list[int]:
    start = time.time()
    for i in nums:
        for j in nums:
            if i + j == target:
                print(f"Total seconds: {time.time() - start}")
                return [i, j]


def two_sum(nums: list[int], target: int) -> list[int]:

    start = time.time()
    num2idx = {n: i for i, n in enumerate(nums)}

    for i in range(len(nums)-1):
        diff = target - nums[i]
        if diff in num2idx and num2idx[diff] != i:
            print(f"Total seconds: {time.time() - start}")
            return [i, num2idx[diff]]


rand_ints = []
for i in range(10000):
    rand_ints.append(random.randint(100, 200))

print(two_sum_inefficient(rand_ints + [10,20,11,15,2,7], 9))
print(two_sum(rand_ints + [10,20,11,15,2,7], 9))



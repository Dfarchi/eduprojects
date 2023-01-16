# Write a function that receives a list of numbers as a parameter.
# The function returns the sum of numbers in the list.
# Arguments types: list
# Return value type: float


def nums_sum(nums: list) -> float:
    total_sum: float = 0.0
    for x in nums:
        total_sum += x
    return total_sum


print(nums_sum([3, 10, 50, -2, 0]))
print(nums_sum([0]))
print(nums_sum([-2]))
print(nums_sum([]))
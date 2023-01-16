# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


def majority_element(nums: list[int]) -> int:
    elem2count: dict[int:int] = {}
    for num in nums:
        if num not in elem2count:
            elem2count[num] = 1
        else:
            elem2count[num] += 1

    max_count = 0
    max_elem = None
    for elem, count in elem2count.items():
        if count > max_count:
            max_elem = elem
            max_count = count

    return max_elem


print(f"Expected output: {3}, actual output: {majority_element([3, 1, 3, 4, 3])}")
print(f"Expected output: {3}, actual output: {majority_element([3,2,3])}")
print(f"Expected output: {2}, actual output: {majority_element([2,2,1,1,1,2,2])}")

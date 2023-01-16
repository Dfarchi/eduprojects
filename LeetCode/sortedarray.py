# def merge(nums1: list[int], nums2: list[int],m,n):
#     # for ind, num1 in enumerate(nums1):
#     #     if not nums2:
#     #         break
#     #     if nums2[0] > num1:
#     #         nums1.insert(ind+1, nums2[0])
#     #         nums2.remove(nums2[0])
#     #         ind += 1
#     # return nums1[:n+m]
#     # ind = 0
#     # while ind < len(nums1):
#     #     if not nums2:
#     #         break
#     #     if nums2[0] > nums1[ind]:
#     #         x = nums2[0]
#     #         y = nums1[ind]
#     #         nums1.insert(ind, nums2[0])
#     #         nums2.remove(nums2[0])
#     #         ind += 1
#     #     ind += 1
#     # return nums1[:n+m]
#
#
#
#
#     #
#     #
#     # for ind, num1 in enumerate(nums1[:m]):
#     #     for num2 in nums2[:n]:
#     #         if num2 > num1:
#     #            nums1.insert(ind+n, num2)
#     #            nums2.remove(num2)
#     #         elif num2 == num1:
#     #              nums1.insert(ind, num2)
#     #              nums2.remove(num2)
#     # return nums1[:n+m]
#     ind2 = 0
#     for ind, num2 in enumerate(nums2[:n]):
#         while ind2 < len(nums1):
#             if num2 > nums1[ind2]:
#                 nums1.insert(ind+1, num2)
#             ind2 += 1
#     return nums1
def another_way(nums1: list[int], nums2: list[int],n,m):

    i1 = 0
    i2 = 0
    while i1 + i2 < m + n + n:
        # if not nums1 or not nums2:
        #     break
        if nums1[i1] == 0 or nums1[i1] > nums2[i2]:
            nums1.insert(i1, nums2[i2])
            i2 += 1
            i1 += 1
        else:
            i1 += 1
    # for num in nums1:
    #     if num == 0:
    #         nums1.remove(num)
    # nums1 = nums1[:n+m]
    return nums1


m = 3
n = 3
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
# print(merge(nums1, nums2, m, n))
print(another_way(nums1, nums2,n,m))


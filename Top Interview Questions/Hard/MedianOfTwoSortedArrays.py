# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


# def arrayMedian(nums):
#     mid = len(nums)//2
#     if len(nums) % 2 == 0:
#         return (nums[mid-1] + nums[mid]) / 2
#     return nums[mid]
#
#
# def bs(l, r, mid, nums1, nums2):
#     while l < r:
#         m = (l + r) // 2
#     x1 = nums2[min(len(nums2), mid - m)]
#     x2 = nums2[max(0, mid - m - 1)]
#     if nums1[m] < :
#         l = m + 1
#     elif nums[m] >= target:
#         r = m
#     return l
#
#
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         n, m = len(nums1), len(nums2)
#         if n == 0:
#             return arrayMedian(nums2)
#         if m == 0:
#             return arrayMedian(nums1)
#         mid = (n + m - 1) // 2
#         mid1 = (n - 1) // 2
#         mid2 = (m - 1) // 2
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.findMedianSortedArrays([2, 4, 4, 5], [1, 3, 6]))

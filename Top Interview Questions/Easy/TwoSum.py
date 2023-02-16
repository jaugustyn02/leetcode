# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def bs(arr, l, r, x):
    while l <= r:
        m = (l+r) // 2
        if(arr[m][0] == x):
            return m
        if(arr[m][0] < x):
            l = m+1
        else:
            r = m-1
    return -1


class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        nums.sort()
        for i in range(n-1):
            x = target - nums[i][0]
            j = bs(nums, i+1, n-1, x)
            if j != -1:
                return nums[i][1], nums[j][1]
        return -1
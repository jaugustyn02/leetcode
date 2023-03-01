# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.


class Solution(object):
    def permute(self, nums):
        result, prefix = [], []
        self.generatePerm(prefix, nums, result)
        return result

    def generatePerm(self, prefix, left, result):
        if not left:
            result.append(prefix)
            return
        for i, x in enumerate(left):
            self.generatePerm(prefix + [x], left[:i] + left[i + 1:], result)

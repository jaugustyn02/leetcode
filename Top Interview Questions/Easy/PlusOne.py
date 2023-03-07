# 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith
# digit of the integer. The digits are ordered from most significant to the least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Time complexity: O(N)
# Space complexity: O(1)

class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] > 9:
                digits[i] -= 10
                digits[i-1] += 1
            else: break
        if digits[0] > 9:
            digits[0] -= 10
            return [1] + digits
        return digits
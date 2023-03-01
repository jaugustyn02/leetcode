# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


class Solution(object):
    def reverse(self, x):
        rev_x = x//max(abs(x),1) * int(str(abs(x))[::-1])
        if rev_x < -pow(2, 31) or rev_x >= pow(2, 31): return 0
        return rev_x
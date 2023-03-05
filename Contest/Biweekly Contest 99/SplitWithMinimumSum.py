# 2578. Split With Minimum Sum

# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
# 1. The concatenation of num1 and num2 is a permutation of num.
#    In other words, the sum of the number of occurrences of each digit in num1 and num2
#    is equal to the number of occurrences of that digit in num.
# 2. num1 and num2 can contain leading zeros.

# Return the minimum possible sum of num1 and num2.

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)


class Solution(object):
    def splitNum(self, num):
        l_num = list(str(num))
        l_num.sort()
        l_num1 = l_num[::2]
        l_num2 = l_num[1::2]
        if not l_num1:
            num1 = 0
        else:
            num1 = int(''.join(l_num1))
        if not l_num2:
            num2 = 0
        else:
            num2 = int(''.join(l_num2))
        return num1 + num2

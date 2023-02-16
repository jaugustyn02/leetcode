# 13. Roman to Integer
# Given a roman numeral, convert it to an integer.

class Solution(object):
    def romanToInt(self, s):
        romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        lsInt = [romanDict[c] for c in s]
        result = 0
        for i in range(len(lsInt)-1):
            if lsInt[i] < lsInt[i+1]:
                result -= lsInt[i]
            else: result += lsInt[i]
        return result + lsInt[-1]

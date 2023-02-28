# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


class Solution(object):
    def longestCommonPrefix(self, strs):
        longestPref = strs[0]
        for s in strs[1:]:
            n = min(len(s), len(longestPref))
            i = 0
            while i < n and s[i] == longestPref[i]:
                i+=1
            longestPref = longestPref[:i]
        return longestPref
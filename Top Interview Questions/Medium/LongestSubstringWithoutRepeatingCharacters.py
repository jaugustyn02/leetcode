# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        contains = [0 for _ in range(128)]
        l, r, max_len = 0, 0, 0
        while r < len(s):
            if contains[ord(s[r])] > 0:
                while l < r and s[l] != s[r]:
                    contains[ord(s[l])] = 0
                    l += 1
                l += 1
            else:
                contains[ord(s[r])] = 1
            r += 1
            max_len = max(max_len, r-l)
        return max_len

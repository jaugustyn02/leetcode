// 28. Find the Index of the First Occurrence in a String
// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
// or -1 if needle is not part of haystack.

// Time complexity: O(N)
// Space complexity: O(1)


class Solution {
public:
    int strStr(string haystack, string needle) {
        return haystack.find(needle);
    }
};
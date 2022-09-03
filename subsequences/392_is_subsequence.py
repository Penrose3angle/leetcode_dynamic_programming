# https://leetcode.com/problems/is-subsequence/
# .Given two subsequences s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)
        if n == 0:
            return True
        # track whether char i in s is found in t
        track = [0] * n
        index = 0

        for i in range(m):
            if index == n:
                break
            if s[index] == t[i]:
                track[index] = 1
                index += 1

        # print(track)
        return bool(track[-1])


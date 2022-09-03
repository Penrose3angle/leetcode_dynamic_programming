# https://leetcode.com/problems/longest-common-subsequence/
# .Given two subsequences text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two subsequences is a subsequence that is common to both subsequences.
#
#
#
# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.a.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # padded track: track longest common sub
        track = [[0] * (n+1) for _ in range(m+1)]

        for r in range(1,m+1):
            for c in range(1,n+1):
                if text1[r-1] == text2[c-1]:
                    # count top-left (this helps in case)
                    track[r][c] = 1 + track[r-1][c-1]
                else:
                    # either from top or left
                    track[r][c] = max(track[r-1][c], track[r][c-1])
        # print(track)
        return track[-1][-1]



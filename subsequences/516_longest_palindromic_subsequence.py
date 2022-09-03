# https://leetcode.com/problems/longest-palindromic-subsequence/
# .Given a string s, find the longest palindromic subsequence's length in s.
#
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:
#
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
#  .

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        # track longest subsequence from s[i: j+1]
        track = [[0] * m for _ in range(m)]
        # single letter is a palindrome
        for i in range(m):
            track[i][i] = 1

        for r in reversed(range(m)):
            for c in range(r + 1, m):
                if s[r] != s[c]:
                    # get max len from left or bottom
                    track[r][c] = max(track[r][c - 1], track[r + 1][c])
                else:
                    # immediate next
                    if c - r == 1:
                        track[r][c] = 1 + track[r][c - 1]
                    # inner substring
                    else:
                        track[r][c] = 2 + track[r + 1][c - 1]

        # print(track)
        return max(track[0])

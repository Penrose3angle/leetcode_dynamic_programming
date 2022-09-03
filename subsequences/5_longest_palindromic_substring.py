# https://leetcode.com/problems/longest-palindromic-substring/
#
# .Given a string s, return the longest palindromic substring in s.
#
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb".

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # track whether s[r:c+1] is palindrome or not
        track = [[0] * n for _ in range(n)]
        longest_palindrome = s[0]
        # a single letter is always a palindrome
        for i in range(n):
            track[i][i] = 1

        for r in reversed(range(n - 1)):
            for c in range(r + 1, n):
                if s[r] != s[c]:
                    track[r][c] = 0
                # if find possible corners of palindrome
                else:
                    # case 1: compare next letter (a+'a')
                    if c - r == 1:
                        track[r][c] = 1
                    # case 2: inner string (r+1, c-1) is also pal -> a + pal = pal
                    elif track[r + 1][c - 1] == 1:
                        track[r][c] = 1

                    # find longest palindrome:
                    if track[r][c] == 1 and len(longest_palindrome) < len(s[r:c + 1]):
                        longest_palindrome = s[r:c + 1]

        # print(track)
        return longest_palindrome
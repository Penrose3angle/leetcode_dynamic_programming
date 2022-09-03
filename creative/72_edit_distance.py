# https://leetcode.com/problems/edit-distance/
#
# .Given two subsequences word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u').

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # padded track min edit distance from word1[:i] to word2[:j]
        track = [[0] * (n + 1) for _ in range(m + 1)]
        track[0][0] = 0  # empty string to empty string

        for c in range(1, n + 1):
            track[0][c] = c  # edit distance from '' to word2[:c]

        for r in range(1, m + 1):
            track[r][0] = r

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if word1[r - 1] == word2[c - 1]:
                    track[r][c] = track[r - 1][c - 1]
                else:
                    track[r][c] = 1 + min(track[r][c - 1],  # + insert word2[c]
                                          track[r - 1][c],  # + delete word1[r]
                                          track[r - 1][c - 1])  # + replace

        # print(track)
        return track[-1][-1]

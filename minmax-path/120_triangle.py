# https://leetcode.com/problems/triangle/
#
# .Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
#
#
#
# Example 1:
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:
#
# Input: triangle = [[-10]]
# Output: -10.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        track = [[0] * i for i in range(1, n + 1)]
        track[-1] = triangle[-1]

        for r in reversed(range(n - 1)):
            for c in range(r + 1):
                candidates = [track[r + 1][c], track[r + 1][c + 1]]
                track[r][c] = triangle[r][c] + min(candidates)

        # print(track)
        return track[0][0]

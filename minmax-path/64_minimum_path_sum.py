# https://leetcode.com/problems/minimum-path-sum/
# .Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # track min path sum starting at (i, j) to (m-1, n-1)
        track = [[0] * n for _ in range(m)]
        track[m - 1][n - 1] = grid[m - 1][n - 1]

        # bottom row can only go right
        for c in reversed(range(n - 1)):
            track[m - 1][c] = track[m - 1][c + 1] + grid[m - 1][c]

        # right most col can only go down
        for r in reversed(range(m - 1)):
            track[r][n - 1] = track[r + 1][n - 1] + grid[r][n - 1]

        # print(track)
        # fill in the rest
        for r in reversed(range(m - 1)):
            for c in reversed(range(n - 1)):
                # can come from either bottom or right
                track[r][c] = min(track[r + 1][c], track[r][c + 1]) + grid[r][c]

        # print(track)

        return track[0][0]

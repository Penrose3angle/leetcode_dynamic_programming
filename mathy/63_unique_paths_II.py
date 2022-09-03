# https://leetcode.com/problems/unique-paths-ii/
# .You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
#
#
#
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # track ways that (i, j) can get to (m-1, n-1)
        track = [[0] * n for _ in range(m)]
        track[m - 1][n - 1] = 1 if obstacleGrid[m - 1][n - 1] == 0 else 0

        # last row
        for c in reversed(range(n - 1)):
            track[m - 1][c] = track[m - 1][c + 1] if obstacleGrid[m - 1][c] == 0 else 0
        # last col
        for r in reversed(range(m - 1)):
            track[r][n - 1] = track[r + 1][n - 1] if obstacleGrid[r][n - 1] == 0 else 0

        for r in reversed(range(m - 1)):
            for c in reversed(range(n - 1)):
                # ways at (r,c) = ways from bottom + ways from right
                track[r][c] = (track[r + 1][c]
                               + track[r][c + 1]) if obstacleGrid[r][c] == 0 else 0

        # print(track)
        return track[0][0]

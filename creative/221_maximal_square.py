# https://leetcode.com/problems/maximal-square/
#
# .Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:
#
# Input: matrix = [["0"]]
# Output: 0
# .

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # track size of square length with (i.j) as bottom right
        track = [[0] * n for _ in range(m)]

        for c in range(n):
            track[0][c] = int(matrix[0][c])

        for r in range(m):
            track[r][0] = int(matrix[r][0])

        for r in range(1, m):
            for c in range(1, n):
                if int(matrix[r][c]) == 0:
                    track[r][c] = 0
                else:
                    # check top, left, diag(top-left)
                    track[r][c] = min(track[r - 1][c],
                                      track[r][c - 1],
                                      track[r - 1][c - 1]) + 1
        # print(track)
        # find maximum
        max_row = [max(row) for row in track]
        max_side = max(max_row)

        return max_side * max_side

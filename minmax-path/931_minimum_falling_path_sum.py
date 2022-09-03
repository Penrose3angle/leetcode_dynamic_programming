# https://leetcode.com/problems/minimum-falling-path-sum/
# .Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
#
#
#
# Example 1:
#
#
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:
#
#
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown..

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # track min sum from lower row
        track = [0] * n
        track = matrix[-1]
        curr = [0] * n

        for r in reversed(range(n - 1)):
            for c in range(n):
                if c == 0:
                    candidates = [track[c], track[c + 1]]
                elif c == n - 1:
                    candidates = [track[c - 1], track[c]]
                else:
                    candidates = [track[c - 1], track[c], track[c + 1]]
                curr[c] = matrix[r][c] + min(candidates)
            # print(track, curr)
            # careful when copy list, if use track=curr, it breaks
            track[:] = curr

        return min(track)

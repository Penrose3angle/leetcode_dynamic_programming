# https://leetcode.com/problems/matrix-block-sum/
# .Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
#
# i - k <= r <= i + k,
# j - k <= c <= j + k, and
# (r, c) is a valid position in the matrix.
#
#
# Example 1:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# Example 2:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
# .

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # padded track sum of mat from (0,0) to (i,j) inclusive
        # i = r+1, j = c+1
        track = [[0] * (n + 1) for _ in range(m + 1)]
        # center pieces
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                track[r][c] = (mat[r - 1][c - 1]
                               + track[r - 1][c]
                               + track[r][c - 1]
                               - track[r - 1][c - 1])
        # print(track)

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                low_r, high_r = max(0, i - k), min(m - 1, i + k)
                low_c, high_c = max(0, j - k), min(n - 1, j + k)
                # print(i, j, low_r, low_c, high_r, high_c)
                # answer = largest - cut_left - cut_top + cut_left_top
                answer[i][j] = (track[high_r + 1][high_c + 1]
                                - track[high_r + 1][low_c]
                                - track[low_r][high_c + 1]
                                + track[low_r][low_c])

        return answer



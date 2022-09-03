# https://leetcode.com/problems/pascals-triangle/
# .Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#
# Input: numRows = 1
# Output: [[1]].

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[0] * row for row in range(1, numRows + 1)]
        tri[0] = [1]
        if numRows == 1:
            return tri

        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    tri[i][j] = 1
                else:
                    tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
        return tri

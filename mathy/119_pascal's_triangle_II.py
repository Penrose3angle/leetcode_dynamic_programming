# https://leetcode.com/problems/pascals-triangle-ii/
# .Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#
# Example 1:
#
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
#
# Input: rowIndex = 0
# Output: [1]
# Example 3:
#
# Input: rowIndex = 1
# Output: [1,1].

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 6C1 *(5) /(2) = 6C2
        num = rowIndex
        denom = 1
        tri_n = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            tri_n[i] = int(tri_n[i-1] * num / denom)
            num  -= 1
            denom += 1
        return tri_n

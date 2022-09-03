# https://leetcode.com/problems/integer-break/
#
# .Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
#
# Return the maximum product you can get.
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# .

class Solution:
    def integerBreak(self, n: int) -> int:
        # track max product from breaking integer i
        track = [0] * (n + 1)
        track[1] = 1

        for i in range(2, n + 1):
            max_product = 0
            for k in range(1, i):
                # either k * (i-k) or k * track[i-k]
                new_product = max(k * (i - k), k * track[i - k])
                max_product = max(max_product, new_product)
            track[i] = max_product
        print(track)
        return track[-1]

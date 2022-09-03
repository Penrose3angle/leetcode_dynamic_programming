# https://leetcode.com/problems/perfect-squares/
#
# .Given an integer n, return the least number of perfect square numbers that sum to n.
#
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
#
#
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9..

class Solution:
    def numSquares(self, n: int) -> int:
        # track min number of perfect square that sum to i
        track = [math.inf] * (n + 1)
        track[0] = 0
        track[1] = 1

        squares = [x * x for x in range(1, n)]

        for i in range(2, n + 1):
            min_num = math.inf
            for sq in squares:
                if i >= sq:
                    # (sq, track[i-sq]) = 1 + track[i-sq]
                    min_num = min(min_num, 1 + track[i - sq])
                else:
                    break
            track[i] = min_num

        print(track)
        return track[-1]

# https://leetcode.com/problems/unique-binary-search-trees/
# .Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
# Example 2:
#
# Input: n = 1
# Output: 1
#  .

class Solution:
    def numTrees(self, n: int) -> int:
        # track number of unique trees given number 1 to i
        track = [0] * (n + 1)
        track[0] = 1  # for transition equation
        track[1] = 1

        for i in range(2, n + 1):
            # track[i] = sum_(root = 1 to i) {track[root-1] * track[i-root]}
            # count = 0
            # for root in range(1, i+1):
            #     # from root, split into two consecutive ranges
            #     # left = range(1, root)
            #     # right = range(root, i)
            #     left_size = root-1
            #     right_size = i-root
            #     count += track[left_size] * track[right_size]
            track[i] = sum([track[root - 1] * track[i - root] for root in range(1, i + 1)])

        # print(track)
        return track[n]

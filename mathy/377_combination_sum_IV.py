# https://leetcode.com/problems/combination-sum-iv/
#
# .Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
#
# The test cases are generated so that the answer can fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:
#
# Input: nums = [9], target = 3
# Output: 0.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # track number of combi add up to i
        track = [0] * (target + 1)
        track[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    track[i] += track[i - n]

        # print(track)
        return track[-1]

#         memo = dict()
#         def combi(target):

#             if memo.get(target) is not None:
#                 return memo[target]

#             if target < min(nums):
#                 memo[target] = 0
#                 return 0

#             else:
#                 count = 0
#                 for num in nums:
#                     if num == target:
#                         count += 1
#                     elif num < target:
#                         count += 1 * combi(target-num)
#                     else:
#                         pass
#                 memo[target] = count
#                 return memo[target]


#         count = combi(target)
#         # print(memo)
#         return count
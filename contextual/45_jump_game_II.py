# https://leetcode.com/problems/jump-game-ii/

# .Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2.

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # track min step from step ith to last index
        tracker = [0] * n
        next_reachable = n - 1
        for i in reversed(range(n - 1)):
            # if reachable:
            max_step = i + nums[i]
            if max_step >= next_reachable:
                # can reach last idx
                if max_step >= n - 1:
                    tracker[i] = 1
                # can reach next reachable
                else:
                    tracker[i] = 1 + min(tracker[i + 1: max_step + 1])
                next_reachable = i
            # unreachable
            else:
                tracker[i] = inf

        # print(tracker)
        return tracker[0]

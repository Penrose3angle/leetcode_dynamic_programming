# https://leetcode.com/problems/jump-game/
# .You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index..

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        # track 0/1 if step ith can reach last index
        tracker = [0] * n
        tracker[-1] = 1
        latest_one = n - 1  # last index

        for i in reversed(range(n - 1)):
            if i + nums[i] >= latest_one:
                tracker[i] = 1
                latest_one = i
            else:
                tracker[i] = 0

        # print(tracker)
        return bool(tracker[0])

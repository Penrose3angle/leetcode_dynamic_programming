# https://leetcode.com/problems/maximum-subarray/
# .Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # track max sum up to index i
        # tracker = [0] * n
        # tracker[0] = nums[0]
        prev_1 = nums[0]
        curr = nums[0]
        max_sum = curr
        # each step has two choice: restart or add-on
        for i in range(1, n):
            # tracker[i] = max(nums[i], tracker[i-1] + nums[i])
            curr = max(nums[i], prev_1 + nums[i])
            max_sum = max(max_sum, curr)
            prev_1 = curr
        # print(tracker)
        # return max(tracker)
        return max_sum

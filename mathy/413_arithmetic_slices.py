# https://leetcode.com/problems/arithmetic-slices/
# .An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.
#
# A subarray is a contiguous subsequence of the array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
# Example 2:
#
# Input: nums = [1]
# Output: 0.

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        # track numbers of arith slices that index i belongs to
        track = [0] * n
        # track distance between i and i-1
        d = [0] * n
        d[1] = nums[1] - nums[0]
        # track[0] and track[1] is always 0
        for i in range(2, n):
            d[i] = nums[i] - nums[i - 1]
            # is arith if d[i] == d[i-1]
            if d[i] == d[i - 1]:
                track[i] = track[i - 1] + 1
            else:
                pass

        print(track)
        print(d)
        return sum(track)


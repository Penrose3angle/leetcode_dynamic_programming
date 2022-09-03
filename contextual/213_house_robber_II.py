# https://leetcode.com/problems/house-robber-ii/
# .You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 3.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        def rob_straight(nums):
            n = len(nums)
            if n <= 2:
                return max(nums)
            # track sum of money up to house i
            tracker = [0] * n
            tracker[:2] = nums[:2]
            tracker[2] = nums[2] + tracker[0]

            for i in range(3, n):
                tracker[i] = nums[i] + max(tracker[i - 2], tracker[i - 3])
            return max(tracker[n - 2:])

        # best rob without first house
        r1 = rob_straight(nums[1:])
        # best rob without last house
        r2 = rob_straight(nums[:-1])
        return max(r1, r2)

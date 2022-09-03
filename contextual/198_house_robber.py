# https://leetcode.com/problems/house-robber/
# .You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# .

class Solution:
    def rob(self, nums: List[int]) -> int:
        # can't rob two adjacent house
        # house i must come from either house i-2 or i-3
        n = len(nums)
        # track sum of money up to house i
        tracker = [0] * n
        tracker[:2] = nums[:2]
        if n < 3:
            return max(nums)

        if n >= 3:
            tracker[2] = nums[2] + tracker[0]

        for i in range(3, n):
            tracker[i] = nums[i] + max(tracker[i - 2], tracker[i - 3])

        # end at either house n (index n-1) or n-1 (index n-2)
        # print(tracker)
        return max(tracker[n - 2:])


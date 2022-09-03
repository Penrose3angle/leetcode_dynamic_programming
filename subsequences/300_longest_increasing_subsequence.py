# https://leetcode.com/problems/longest-increasing-subsequence/
#
# .Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
#
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # track max lis if pick a subsequence end with nums[i]
        track = [0] * n
        track[0] = 1

        for i in range(1, n):
            max_lis_j = 0
            # check with previous indices
            for j in range(i):
                if nums[j] < nums[i]:
                    # check max_lis_i
                    max_lis_j = max(max_lis_j, track[j])
            track[i] = max_lis_j + 1

        # print(track)

        return max(track)

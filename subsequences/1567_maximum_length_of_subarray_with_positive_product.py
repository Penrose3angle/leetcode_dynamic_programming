# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# .1567. Maximum Length of Subarray With Positive Product
# Medium
#
# 1773
#
# 43
#
# Add to List
#
# Share
# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
#
# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
#
# Return the maximum length of a subarray with positive product.
#
#
#
# Example 1:
#
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.
# Example 2:
#
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
# Example 3:
#
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3]..

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)

        # track max len of positive and negative product subarray upto index i
        # track_pos = [0] * n
        # track_neg = [0] * n
        # note that both track_x[0] = 0 if nums[0] == 0
        # track_pos[0] = 1 if nums[0] > 0 else 0
        # track_neg[0] = 1 if nums[0] < 0 else 0
        prev_pos_1 = 1 if nums[0] > 0 else 0
        prev_neg_1 = 1 if nums[0] < 0 else 0
        max_len = prev_pos_1

        for i in range(1, n):
            if nums[i] > 0:
                # track_pos[i] = track_pos[i-1] + 1
                # track_neg[i] = track_neg[i-1] + 1 if track_neg[i-1] > 0 else 0
                curr_pos = prev_pos_1 + 1
                # conditional since if prev_neg_1 == 0, it means there's no way to flip the sign
                curr_neg = prev_neg_1 + 1 if prev_neg_1 > 0 else 0
            # found 0, must reset
            elif nums[i] == 0:
                # track_pos[i] = 0
                # track_neg[i] = 0
                curr_pos = 0
                curr_neg = 0
            # flip sign
            else:
                # track_pos[i] = track_neg[i-1] + 1 if track_neg[i-1] > 0 else 0
                # track_neg[i] = track_pos[i-1] + 1
                # conditional since if prev_neg_1 == 0, it means there's no way to flip the sign
                curr_pos = prev_neg_1 + 1 if prev_neg_1 > 0 else 0
                curr_neg = prev_pos_1 + 1

            # find absolute max
            max_len = max(max_len, curr_pos)

            # update
            prev_pos_1 = curr_pos
            prev_neg_1 = curr_neg

        # print(track_pos, track_neg)
        # return max(track_pos)
        return max_len
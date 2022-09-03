# https://leetcode.com/problems/maximum-product-subarray/
# .Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.
#
#
#
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# .

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # track max product found until index i
        # track_max = [0] * n
        # track_max[0] = nums[0]
        # max till index i-1
        prev_max_1 = nums[0]
        # absolute max so far
        max_prod = nums[0]

        # track_min = [0] * n
        # track_min[0] = nums[0]
        # min till index i-1
        prev_min_1 = nums[0]
        # absolute min so far
        min_prod = nums[0]

        for i in range(1, n):
            # each i, choice: reset or continue
            # case 1: no flip sign
            if nums[i] >= 0:
                # track_max[i] = max(nums[i], nums[i] * track_max[i-1])
                # track_min[i] = min(nums[i], nums[i] * track_min[i-1])
                # best action at index i
                curr_max = max(nums[i], nums[i] * prev_max_1)
                curr_min = min(nums[i], nums[i] * prev_min_1)

            # case 2: negative number will flip the sign
            else:
                # nums[i] * track_min[i-1] will flip the sign and will be larger than nums[i] * track_max[i-1]
                # track_max[i] = max(nums[i], nums[i] * track_min[i-1])
                # track_min[i] = min(nums[i], nums[i] * track_max[i-1])
                curr_max = max(nums[i], nums[i] * prev_min_1)
                curr_min = min(nums[i], nums[i] * prev_max_1)

            # find absolute vals so far
            max_prod = max(max_prod, curr_max)
            min_prod = min(min_prod, curr_min)

            # update
            prev_max_1 = curr_max
            prev_min_1 = curr_min

        # print(track_max, track_min)
        # return max(track_max + track_min)
        return max_prod

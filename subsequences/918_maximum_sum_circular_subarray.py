# https://leetcode.com/problems/maximum-sum-circular-subarray/
# .Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
#
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
#
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
#
#
#
# Example 1:
#
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:
#
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:
#
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2..

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return sum(nums)

        def maxSubarray(nums):
            n = len(nums)
            prev_1 = nums[0]
            curr = nums[0]
            max_sum = curr
            # each step has two choice: restart or add-on
            for i in range(1, n):
                curr = max(nums[i], prev_1 + nums[i])
                max_sum = max(max_sum, curr)
                prev_1 = curr
            return max_sum

        # answer can be either one-interval array or two-interval array
        # one interval array is like before
        best_one = maxSubarray(nums)

        # two-interval array: find one-interval array that sums to min
        # then find the inverse: sums(nums) - one-interval minSubarray = two-interval maxSubarray
        # find the one-interval minSubarray by finding the max of negative version
        # note the index must be between 1 - n-2 only to make sure the answer is two-interval
        neg = [-n for n in nums]
        # print(neg)
        best_two = sum(nums) + maxSubarray(neg[1:n - 1])
        return max(best_one, best_two)



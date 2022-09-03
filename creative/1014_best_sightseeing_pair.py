# https://leetcode.com/problems/best-sightseeing-pair/
# .You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
#
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
#
# Return the maximum score of a pair of sightseeing spots.
#
#
#
# Example 1:
#
# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
# Example 2:
#
# Input: values = [1,2]
# Output: 2
# .

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        left = 0
        right = 1
        max_val = 0

        # i < j
        # val(i, r) = values[i] + values[r] + i - r for r > j > i
        # val(j, r) = values[j] + values[r] + j - r for r > j > i
        # dominance: j dominates i if val(i, r) < val(j, r) for all r > j > i
        # <=> values[i] + values[r] + i - r < values[j] + values[r] + j - r
        # <=> values[i] + i < values[j] + j
        # If values[i] + i < values[j] + j, better to restart search from index j
        # otherwise, continue to add right index
        while right < n:
            curr_val = values[left] + values[right] + left - right
            max_val = max(max_val, curr_val)
            if values[left] + left < values[right] + right:  # reset
                left = right
            right += 1

        return max_val

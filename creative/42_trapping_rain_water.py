# https://leetcode.com/problems/trapping-rain-water/
# .Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
# .

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # water level at step i depends maximum height from the left side, the maximum height from the right side, and the height of the bar at i

        # track max height from left
        max_h_left = [0] * n
        # track max height from right
        max_h_right = [0] * n
        # track trapped water at each index
        water_level = [0] * n

        max_h_left[0] = height[0]
        max_h_right[-1] = height[-1]

        for i in range(1, n):
            max_h_left[i] = max(max_h_left[i - 1], height[i])

        for i in reversed(range(0, n - 1)):
            max_h_right[i] = max(max_h_right[i + 1], height[i])

        # print(max_h_left)
        # print(max_h_right)
        for i in range(1, n):
            water_level[i] = min(max_h_left[i], max_h_right[i]) - height[i]
        # print(water_level)
        return sum(water_level)

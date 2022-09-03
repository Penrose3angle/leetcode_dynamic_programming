# https://leetcode.com/problems/min-cost-climbing-stairs/
# .You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
#
# Example 1:
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6..

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # can climb 1 or 2 steps
        n = len(cost)
        if n == 1:
            return 0

        # track: sum cost up to step i if step on it
        # min_cost = [0] * n
        # first two steps
        min_cost_prev_2 = cost[0]
        min_cost_prev_1 = cost[1]
        # min_cost[:2] = cost[:2]
        # from step i can go to either i+1 or i+2
        # in other words, at step i, the min cost is
        # cost[i] + min(min_cost[i-1], min_cost[i-2])

        for i in range(2, n):
            # min_cost[i] = cost[i] + min(min_cost[i-1], min_cost[i-2])
            min_cost_cur = cost[i] + min(min_cost_prev_1, min_cost_prev_2)
            min_cost_prev_2 = min_cost_prev_1
            min_cost_prev_1 = min_cost_cur

        # print(min_cost)
        # choose whichever step has the least cost from the last two steps
        # return min(min_cost[n-2:])
        return min(min_cost_prev_1, min_cost_prev_2)

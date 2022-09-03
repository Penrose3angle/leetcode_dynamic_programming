# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# .You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0..

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # track best money-on-hands in each state at step i
        track_blank = [0] * n
        track_hold = [0] * n
        track_end = [0] * n
        track_hold[0] = - prices[0]

        for i in range(1, n):
            # must come from (blank, none)
            track_blank[i] = track_blank[i - 1]
            # either from (hold, none) or (blank, buy)
            track_hold[i] = max(track_hold[i - 1], track_blank[i - 1] - prices[i])
            # must come fro (hold, sell)
            track_end[i] = track_hold[i - 1] + prices[i]

        print(track_blank)
        print(track_hold)
        print(track_end)

        # optimal must end with state end
        return max(track_end)

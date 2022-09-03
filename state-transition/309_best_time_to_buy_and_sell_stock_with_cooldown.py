# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# .You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
#
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#
#
# Example 1:
#
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:
#
# Input: prices = [1]
# Output: 0
# .

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        track_blank = [0] * n
        track_hold = [0] * n
        track_cool = [0] * n

        # at i = 0, if we buy
        track_hold[0] = - prices[0]

        for i in range(1, n):
            # either from (blank, none) or (cool, none)
            track_blank[i] = max(track_blank[i - 1], track_cool[i - 1])
            # either from (hold, none) or (blank, buy)
            track_hold[i] = max(track_hold[i - 1], track_blank[i - 1] - prices[i])
            # must be from (hold, sell)
            track_cool[i] = track_hold[i - 1] + prices[i]

        # print(track_blank)
        # print(track_hold)
        # print(track_cool)

        # optimal state in either blank or cool state
        return max(track_blank + track_cool)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# .You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#
#
# Example 1:
#
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Example 2:
#
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
# .

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        track_blank = [0] * n
        track_hold = [0] * n
        track_hold[0] = -prices[0]

        for i in range(1, n):
            # either from (blank, none) or (hold, sell with fee)
            track_blank[i] = max(track_blank[i - 1],
                                 track_hold[i - 1] + prices[i] - fee)
            # either from (hold, none) or (blank, buy)
            track_hold[i] = max(track_hold[i - 1],
                                track_blank[i - 1] - prices[i])

        # print(track_blank)
        # print(track_hold)

        return max(track_blank)

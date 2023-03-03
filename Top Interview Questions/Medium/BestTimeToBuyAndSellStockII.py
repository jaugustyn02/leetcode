# 122. Best Time to Buy and Sell Stock II
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.


class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        buy, sell, prof = prices[0], None, 0
        for price in prices[1:]:
            if sell is None and (buy is None or price <= buy):
                buy = price
            elif sell is None or price > sell:
                sell = price
            elif sell > buy:
                prof += sell - buy
                buy, sell = price, None
        if sell is not None and sell > buy:
            prof += sell - buy
        return prof

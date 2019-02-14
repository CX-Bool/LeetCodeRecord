# 执行用时: 52 ms, 在Best Time to Buy and Sell Stock II的Python3提交中击败了93.71% 的用户
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        maxPrice = minPrice = prices[0]
        for price in prices:
            if price > maxPrice:
                maxPrice = price
            else:
                profit += maxPrice - minPrice
                maxPrice = minPrice = price
        profit += maxPrice - minPrice
        return profit
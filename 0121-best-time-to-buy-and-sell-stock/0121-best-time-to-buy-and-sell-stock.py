class Solution(object):
    def maxProfit(self, prices):
        min_buy=prices[0]
        max_profit=0
        for price in prices:
            if price<min_buy:
                min_buy=price
            profit=price-min_buy
            if profit>max_profit:
                max_profit=profit

        
        return max_profit
        
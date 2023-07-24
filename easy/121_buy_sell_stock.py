class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0
        for v in prices:
            lowest = min(lowest,v)
            profit = v-lowest
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit



[13,1,4,2,7,3,8,2]

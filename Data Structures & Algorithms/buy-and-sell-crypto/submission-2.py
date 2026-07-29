class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0
        # use sliding window and when you get negative, shift l to that point
        if len(prices) <= 1:
            return 0

        for r in range(len(prices)):
            if l == r:
                continue
            profit = prices[r] - prices[l]

            if profit >= 0:
                maxProfit = max(maxProfit, profit)
            else:
                l = r
        
        return maxProfit



            

            
            

        
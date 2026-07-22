class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        # smallest value should be to the left of the largest value
        

        l = 0
        r = 1
        maxDiff = 0

        while l < len(prices) - 1 and r < len(prices):
            diff = prices[r] - prices[l]
            
            if diff > 0 and diff > maxDiff:
                maxDiff = diff
                r += 1
            elif diff > 0:
                r += 1
            else:
                l = r
                r = l + 1
        
        return maxDiff


            

            
            

        
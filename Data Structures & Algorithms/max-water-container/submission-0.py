class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxVol = 0

        if len(heights) <= 1:
            return 0

        while l < r:
            width = r - l
            h1 = heights[l]
            h2 = heights[r]
            vol = 0

            if h1 < h2:
                vol = width * h1
                l += 1
            else:
                vol = width * h2
                r -= 1
            if vol > maxVol:
                maxVol = vol
        
        return maxVol
            
            



        
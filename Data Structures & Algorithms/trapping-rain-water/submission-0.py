class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax, rightMax = height[l], height[r]
        aggregate = 0
        
        if not height:
            return 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                if leftMax - height[l] >= 0:
                    aggregate += (leftMax - height[l])

            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                if rightMax - height[r] >= 0:
                    aggregate += (rightMax - height[r])
        
        return aggregate

        
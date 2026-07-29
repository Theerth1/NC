class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # in each window, check most occurring char and that window is good if 
        # window - mostOccur >= k
        # once it fails, increment (l += 1) and best case scenario becomes best -= 1

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
    
        hashMap = {}
        l = 0
        windowSize = 0
        bestWindowSize = 0
        
        
        for r in range(len(s)):
            windowSize = r - l + 1

            if s[r] not in hashMap:
                hashMap[s[r]] = 1
            else:
                hashMap[s[r]] += 1
            
            while windowSize - max(list(hashMap.values())) > k:
                hashMap[s[l]] -= 1
                l += 1
                windowSize -= 1
            if windowSize > bestWindowSize:
                bestWindowSize = windowSize

        return bestWindowSize
            

            
        


        
        
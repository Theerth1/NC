class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # each substring is allowed to progress if len(substring) <= k OR len(substring) - mostOccur <= k
        # if that substring fails, we increment L by 1 and recompute (while loop is optimal here)
        # as we remove, we need to update stringDict
        stringDict = {}
        L = 0
        maxLength = 0

        for R in range(len(s)):
            if s[R] not in stringDict:
                stringDict[s[R]] = 1
            else:
                stringDict[s[R]] += 1
            
            if (R - L + 1) <= k or (R - L + 1 - max(stringDict.values())) <= k:
                maxLength = max(maxLength, R - L + 1)
                continue
            else:
                while (R - L + 1) > k and (R - L + 1 - max(list(stringDict.values()))) > k:
                    stringDict[s[L]] -= 1
                    L += 1
            maxLength = max(maxLength, R - L + 1)
        
        return maxLength


                



        
            

            
        


        
        
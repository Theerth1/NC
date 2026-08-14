class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window approach

        if added character is homogenous with substring:
            keep increasing
        else:
            move left pointer past the disrupting character
            this is new window
        
        """

        L = 0

        discreteSet = set()
        maxLength = 0

        for R in range(len(s)):
            if s[R] not in discreteSet:
                discreteSet.add(s[R])
                maxLength = max(maxLength, R - L + 1)
            else:
                while s[L] != s[R]:
                    discreteSet.remove(s[L])
                    L += 1
                discreteSet.remove(s[L])
                L += 1
                discreteSet.add(s[R])
                maxLength = max(maxLength, R - L + 1)
        
        return maxLength


            
            
        
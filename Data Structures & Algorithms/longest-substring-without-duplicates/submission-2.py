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

        l = 0
        discreteChars = set()
        largest = 0

        for r in range(len(s)):
            if s[r] not in discreteChars:
                discreteChars.add(s[r])
            else:
                while s[l] != s[r]:
                    l += 1
                l += 1
                discreteChars = set(s[l:r + 1])
            largest = max(largest, r - l + 1)

        return largest

            
            
        
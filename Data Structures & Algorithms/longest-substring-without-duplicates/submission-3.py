class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l = 0
        r = 0
        seen = set()
        maxLength = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                maxLength = max(maxLength, r - l + 1)
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
                maxLength = max(maxLength, r - l + 1)
        
        return maxLength
            









        
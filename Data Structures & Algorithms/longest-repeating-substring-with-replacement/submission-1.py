class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        l = 0
        hashmap = {}

        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] += 1
            # mostOccur = max(hashmap.values())

            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
                #mostOccur = max(hashmap.values())
            
            longest = max(longest, r - l + 1)

        return longest



        
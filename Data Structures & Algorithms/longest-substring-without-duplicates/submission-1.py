class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        "aab"
        l = 0
        r = 1
        seen = set()
        seen.add(s[l])
        curr = s[l]
        longest = 1


        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                curr += s[r]
                longest = max(longest, len(curr))
                r += 1  
            else:
                #need to remove all letters including first occurrence of s[r]
                store = -1
                for i in range(len(curr)):
                    if curr[i] == s[r]:
                        store = i
                        break
                curr = curr[store + 1:]
                longest = max(longest, len(curr))
                seen.clear()
                seen.update(curr)
                l += store + 1
                #need to update pointers based off where the window sits inside string s
        return longest









        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        oracleDict = {}
        for char in s1:
            if char not in oracleDict:
                oracleDict[char] = 1
            else:
                oracleDict[char] += 1
        
        l = 0
        r = len(s1) - 1

        windowDict = {}
        for i in range(l, r + 1):
            if s2[i] not in windowDict:
                windowDict[s2[i]] = 1
            else:
                windowDict[s2[i]] += 1

        while not windowDict == oracleDict:
            windowDict[s2[l]] -= 1
            if windowDict[s2[l]] == 0:
                del windowDict[s2[l]]
            l += 1
            r += 1
            if r >= len(s2):
                return False
            if s2[r] not in windowDict:
                windowDict[s2[r]] = 1
            else:
                windowDict[s2[r]] += 1

            
        
        return True

        

        

        
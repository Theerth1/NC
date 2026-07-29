class Solution:
    def permute(self, subString: str) -> bool:
        map2 = {}

        for char in subString:
            if char not in map2:
                map2[char] = 1
            else:
                map2[char] += 1
        
        return Solution.oracleDict == map2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        Solution.oracleDict = {}
        for char in s1:
            if char not in Solution.oracleDict:
                Solution.oracleDict[char] = 1
            else:
                Solution.oracleDict[char] += 1
        
        l = 0
        r = len(s1) - 1


        while not self.permute(s2[l:r+1]):
            l += 1
            r += 1

            if r > len(s2):
                return False
        
        return True

        

        

        
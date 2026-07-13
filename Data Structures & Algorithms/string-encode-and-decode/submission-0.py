class Solution:

    def encode(self, strs: List[str]) -> str:
       strLength = "," + str(len(strs))
       key = ""
       encoded = ""
       for s in strs:
           key += f"{len(s)};"
           encoded += s
       key = key + ","

       encoded = key + encoded + strLength
       return encoded

    def decode(self, s: str) -> List[str]:
        store = 0
        for i in range(len(s)):
            if s[i] == ",":
                store = i
        
        length = int(s[store + 1:])
        decoded = []
        s = s[:store]

        firstComma = 0
        for i in range(len(s)):
            if s[i] == ",":
                firstComma = i
                break

        key = s[:firstComma]
        s = s[firstComma + 1:]

    
        individualLengths = []
        key = key.split(";")

        for i in range(length):
            k = int(key[i])
            decoded.append(s[:k])
            s = s[k:]
        
        return decoded






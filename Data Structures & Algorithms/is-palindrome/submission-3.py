import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        clean = ""
        for char in s:
            if char.isdigit():
                clean += (char)
            elif char in string.ascii_letters:
                clean += (char.lower())
        l = 0
        r = len(clean) - 1

        #even vs odd
        # if even: "abab" if l = r -1 then stop
        # if odd: "ababa" if l = r -2 then stop
        if not clean:
            return True

        if len(clean) % 2 == 0:
            while not (l > r):
                if clean[l] == clean[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        else:
            while not (l == r):
                if clean[l] == clean[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        """
        clean = ""
        for char in s:
            if char.isdigit():
                clean += (char)
            elif char in string.ascii_letters:
                clean += (char.lower())
        return clean == clean[::-1]
        
class Solution:
    def longestPalindrome(self, s: str) -> int:
        charSet = set()
        lngLength = 0
        for char in s:
            if char in charSet:
                lngLength += 2
                charSet.remove(char)
            else:
                charSet.add(char)

        return lngLength + 1 if charSet else lngLength

            



        

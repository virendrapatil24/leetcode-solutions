class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char = 0
        for sChar in s: char ^= ord(sChar)
        for tChar in t: char ^= ord(tChar)
        return chr(char)

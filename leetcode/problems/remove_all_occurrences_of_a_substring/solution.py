class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            l = s.index(part) 
            s = s[:l] + s[l+len(part):]
        return s
        
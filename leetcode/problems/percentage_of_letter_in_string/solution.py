class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        N = len(s)
        if letter in s:
            C = s.count(letter)
        else: return 0
        
        res = C/N*100
        return int(res)
        
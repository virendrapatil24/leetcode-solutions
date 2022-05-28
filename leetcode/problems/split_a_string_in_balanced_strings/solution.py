class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cR, cL, res = 0, 0, 0
        
        for i in s:
            if i == "R":
                cR += 1
            if i == "L":
                cL += 1
            if cR == cL:
                res += 1
                cR, cL = 0, 0
        return res
                
class Solution:
    def partitionString(self, s: str) -> int:
        sSet = set()
        res = 1
        for char in s:
            if char in sSet:
                res += 1
                sSet = set()
                sSet.add(char)
            else:
                sSet.add(char)
        return res 
        
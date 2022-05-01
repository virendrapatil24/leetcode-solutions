class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = []
        lt = []
        for i in s:
            if ls == [] and i == '#': continue
            if i == '#': ls.pop()
            else: ls.append(i)
        for i in t:
            if lt == [] and i == '#': continue
            if i == '#': lt.pop()
            else: lt.append(i)
        
        if ls == lt: return True
        else: return False
            
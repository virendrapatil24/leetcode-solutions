class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        cnt = 0
        for ch in s:
            if ch == "(":
                if cnt: 
                    res += ch
                cnt += 1
            else:
                cnt -= 1
                if cnt:
                    res += ch
        return res
        

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            else:
                if char == ")":
                    if stack:
                        stack.pop()
                    else:
                        s[idx] = ""
        
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)


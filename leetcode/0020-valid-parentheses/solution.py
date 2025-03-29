class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1: return False
        para_map = {'(':')','{':'}','[':']'}
        stack = []
        for char in s:
            if char in para_map:
                stack.append(char)
            elif not stack or char != para_map[stack.pop()]:
                return False
        return len(stack) == 0


        

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        isMatch = {"(":")", "{":"}", "[":"]"}
        stack = []
        for char in s:
            if char in isMatch:
                stack.append(char)
            elif not stack or isMatch[stack.pop()] != char:
                return False
        return len(stack) == 0

        

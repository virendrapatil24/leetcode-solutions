class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif len(stack) == 0 or brackets[stack.pop()] != char:
                return False
        return len(stack) == 0
        
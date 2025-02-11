class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        stack = []
        n = len(part)

        for char in s:
            stack.append(char)

            check_strg = "".join(stack)
            if len(check_strg) >= n and check_strg[-n:] == part:
                for _ in range(n):
                    stack.pop()
        
        return "".join(stack)

        
        
        

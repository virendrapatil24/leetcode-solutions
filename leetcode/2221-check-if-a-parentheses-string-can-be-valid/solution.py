class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        ob_stack = []
        ul_stack = []
        for i in range(len(s)):
            if locked[i] == "0":
                ul_stack.append(i)
            elif s[i] == "(":
                ob_stack.append(i)
            else:
                if ob_stack:
                    ob_stack.pop()
                elif ul_stack:
                    ul_stack.pop()
                else:
                    return False
        
        while ob_stack and ul_stack and ob_stack[-1] < ul_stack[-1]:
            ob_stack.pop()
            ul_stack.pop()

        return ob_stack == []

        

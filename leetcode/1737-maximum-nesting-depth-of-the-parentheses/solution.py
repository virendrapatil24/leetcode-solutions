class Solution:
    def maxDepth(self, s: str) -> int:
        depth, max_depth = 0, 0
        for char in s:
            if char == "(":
                depth += 1
            elif char == ")":
                max_depth = max(max_depth, depth)
                depth -= 1
        return max_depth

        

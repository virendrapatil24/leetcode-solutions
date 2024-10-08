class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        while start or goal:
            if start % 2 != goal % 2: res += 1
            start, goal = start // 2, goal // 2
        return res

        

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        i, j =  1, 1
        for k in range(1, n):
            i, j = j, i+j
        return j

    

        
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for j in range(n):
            res ^= start + 2 * j
        return res
        
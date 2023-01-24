class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(max(t_row) for t_row in zip(*[sorted(row) for row in grid]))
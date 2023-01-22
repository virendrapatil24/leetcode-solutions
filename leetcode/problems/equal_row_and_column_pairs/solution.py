class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_t = Counter(zip(*grid))
        grid = Counter(map(tuple, grid))
        return sum(grid[i]*grid_t[i] for i in grid_t)
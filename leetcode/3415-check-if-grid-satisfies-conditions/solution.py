class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for col in range(1, len(grid[0])):
            if grid[0][col] == grid[0][col - 1]:
                return False
        for row in range(1, len(grid)):
            if grid[row] != grid[row - 1]:
                return False
        return True

        

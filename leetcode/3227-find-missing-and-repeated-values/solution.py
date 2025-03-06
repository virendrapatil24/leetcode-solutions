class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid_set = set()
        grid_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in grid_set:
                    repeating = grid[i][j]
                else:
                    grid_sum += grid[i][j]
                    grid_set.add(grid[i][j])
        n = len(grid) 
        n = n * n
        n_total = (n * (n + 1) // 2)
        missing = n_total - grid_sum
        return [repeating, missing]
        

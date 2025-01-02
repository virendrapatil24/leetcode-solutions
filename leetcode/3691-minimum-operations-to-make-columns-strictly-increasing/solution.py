class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0
        for i in range(len(grid[0])):
            for j in range(len(grid) - 1):
                if grid[j + 1][i] <= grid[j][i]:
                    diff = grid[j][i] - grid[j + 1][i]
                    operations += diff + 1
                    grid[j + 1][i] += diff + 1
        return operations

        

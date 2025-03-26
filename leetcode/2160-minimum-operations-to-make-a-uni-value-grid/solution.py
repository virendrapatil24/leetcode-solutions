class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr_grid = []
        for row in grid:
            arr_grid += row
        arr_grid.sort()
        
        target = arr_grid[len(arr_grid) // 2]
        ops = abs(target - arr_grid[0]) // x
        for i in range(1, len(arr_grid)):
            if arr_grid[i - 1] % x != arr_grid[i] % x:
                return -1
            ops += abs(target - arr_grid[i]) // x
        
        return ops
        

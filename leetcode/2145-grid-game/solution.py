class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_sum1 = [0] * n    
        prefix_sum2 = [0] * n
        prefix_sum1[0] = grid[0][0]
        prefix_sum2[0] = grid[1][0]
        for i in range(1, n):
            prefix_sum1[i] = prefix_sum1[i - 1] + grid[0][i]
            prefix_sum2[i] = prefix_sum2[i - 1] + grid[1][i]
        
        points = inf
        for i in range(n):
            top = prefix_sum1[-1] - prefix_sum1[i]
            bottom = prefix_sum2[i - 1] if i > 0 else 0
            second_robot = max(top, bottom)
            points = min(points, second_robot)

        return points



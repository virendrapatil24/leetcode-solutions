class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or visited[r][c]):
                return 0
            
            visited[r][c] = True
            res = grid[r][c]
            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in nei:
                res += dfs(nr, nc)
            
            return res

        visited = [[0] * COLS for _ in range(ROWS)]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0 and not visited[r][c]:
                    res = max(res, dfs(r, c))
        
        return res
        

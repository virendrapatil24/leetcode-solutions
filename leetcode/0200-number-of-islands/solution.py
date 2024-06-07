class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for i in range(4):
                    r, c = row + dr[i], col + dc[i]
                    if (0 <= r < rows and 
                        0 <= c < cols and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands

        


        

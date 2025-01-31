class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, curr_island):
            grid[r][c] = curr_island
            curr_area = 1
            nei = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            for nr, nc in nei:
                if (nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or
                    grid[nr][nc] != 1):
                    continue
                curr_area += dfs(nr, nc, curr_island)
            return curr_area
        
        def connect(r, c):
            visit = set([0])
            nei = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]

            area = 1
            for nr, nc in nei:
                if (nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or
                    grid[nr][nc] in visit):
                    continue
                area += area_map[grid[nr][nc]]
                visit.add(grid[nr][nc])
            
            return area

        curr_island = 2
        area_map = {}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area_map[curr_island] = dfs(r, c, curr_island)
                    curr_island += 1

        max_area = 0 if not area_map else max(area_map.values())
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    max_area = max(connect(r, c), max_area)

        return max_area 
                    

        

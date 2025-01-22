class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        
        res = [[-1] * COLS for _ in range(ROWS)]
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0
        
        while q:
            r, c = q.popleft()
            h = res[r][c]

            neighbours = [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)] 
            for nr, nc in neighbours:
                if (nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or 
                    res[nr][nc] != -1):
                    continue
                res[nr][nc] = h + 1
                q.append((nr, nc))
        
        return res
        

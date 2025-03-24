class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r >= rows or c >= cols or
                r < 0 or c < 0 or
                board[r][c] != word[i] or 
                (r, c) in visited):
                return False
            
            visited.add((r, c))
            neigbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neigbours:
                if dfs(nr, nc, i + 1):
                    return True
            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
        

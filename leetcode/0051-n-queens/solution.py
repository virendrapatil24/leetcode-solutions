class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_dia = set()
        neg_dia = set()

        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r - c) in neg_dia or (r + c) in pos_dia:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                pos_dia.add(r + c)
                neg_dia.add(r - c)
                dfs(r + 1)
                neg_dia.remove(r - c)
                pos_dia.remove(r + c)
                cols.remove(c)
                board[r][c] = "."
        
        dfs(0)
        return res



        

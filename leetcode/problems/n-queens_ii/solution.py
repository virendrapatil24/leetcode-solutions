class Solution:
    def totalNQueens(self, n: int) -> int:
        
        if n == 0: return []
        
        col = set()
        diagonal = set()
        antidiagonal = set()
        total = []
        res = []
        
        def backtrack(r):
            
            nonlocal n, col, diagonal, antidiagonal, total, res
            
            if r == n:
                res.append(total[:])
                return 
            
            for c in range(n):
                
                if c in col or (r+c) in diagonal or (r-c) in antidiagonal:
                    continue

                col.add(c)
                diagonal.add(r+c)
                antidiagonal.add(r-c)
                total.append('.'*c + 'Q' + '.'*(n-c+1))
                
                backtrack(r+1)
                
                col.remove(c)
                diagonal.remove(r+c)
                antidiagonal.remove(r-c)
                total.pop()
        
        backtrack(0)
        return len(res)              
                
                
                
                
                
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        if n == 0: return []
        
        col = set()
        diagonal = set()    # determined by r+c
        antidiagonal = set() #
        output = []
        result = []
        
        def backtrack(r):
            nonlocal n,col,diagonal,antidiagonal,output,result
            if r == n:
                result.append(output[:])
                return
            
            for c in range(n):
                if c in col or (r+c) in diagonal or (r-c) in antidiagonal: continue
                
                col.add(c)
                diagonal.add(r+c)
                antidiagonal.add(r-c)
                output.append('.'*c + 'Q' + '.'*(n-c-1))
                backtrack(r+1)
                
                col.remove(c)
                diagonal.remove(r+c)
                antidiagonal.remove(r-c)
                output.pop()
        
        backtrack(0)
        return result
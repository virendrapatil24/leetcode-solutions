class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        max_r = []
        max_c = []
        
        for i in range(len(grid)):
            max_r.append(max(grid[i]))
            c = 0
            for j in range(len(grid)):
                c = max(c, grid[j][i])
            max_c.append(c)
         
        max_h = []
        
        for i in max_r:
            max_h1 = []
            for j in max_c:
                max_h1.append(min(i,j))
            max_h.append(max_h1)
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                ans += abs(grid[i][j] - max_h[i][j])
        
        return ans
                
            
            
                
        
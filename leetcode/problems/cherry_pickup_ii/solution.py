class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pos_cherry = {(0, n-1): grid[0][0] + grid[0][-1]}
        for i in range(1, m):
            new = {}
            for (x,y),val in pos_cherry.items():
                robot1 = [a for a in [x-1, x, x+1] if 0 <= a <n]
                robot2 = [b for b in [y-1, y, y+1] if 0 <= b <n]
                for a in robot1:
                    for b in robot2:
                        new_val = val + grid[i][a] + grid[i][b] * (a!=b)
                        if (a, b) not in new or new_val > new[(a,b)]:
                            new[(a,b)] = new_val
            pos_cherry = new
        
        return max(pos_cherry.values())
        
        
        
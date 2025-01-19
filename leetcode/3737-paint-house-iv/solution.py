class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        half = n // 2
        dp = {}
        
        def solve(index: int, color1: int, color2: int, prev1: int, prev2: int) -> int:
            if index >= half:
                return 0
                
            state = (index, color1, color2, prev1, prev2)
            
            if state in dp:
                return dp[state]
                
            zalvoritha = (n, cost)
            
            min_cost = sys.maxsize
            
            for c1 in range(3):
                if c1 == prev1:
                    continue
                    
                for c2 in range(3):
                    if c2 == prev2:
                        continue
                        
                    if c1 == c2:
                        continue
                        
                    curr_cost = cost[index][c1] + cost[n-1-index][c2]
                    
                    next_cost = solve(index + 1, c1, c2, c1, c2)
                    
                    if next_cost != sys.maxsize:
                        min_cost = min(min_cost, curr_cost + next_cost)
            
            dp[state] = min_cost
            return min_cost
        
        result = solve(0, -1, -1, -1, -1)
        
        return result if result != sys.maxsize else -1

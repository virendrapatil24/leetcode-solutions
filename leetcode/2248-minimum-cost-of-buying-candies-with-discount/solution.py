class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        for i in range(0, len(cost), 3):
            if i + 3 > len(cost):
                break
            cost[i+2] = 0
        return sum(cost)
            
        

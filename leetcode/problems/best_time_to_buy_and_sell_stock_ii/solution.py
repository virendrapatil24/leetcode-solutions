class Solution:
    def maxProfit(self, P: List[int]) -> int:
        gains = []
        for i in range(len(P)-1):
            
            if P[i+1] - P[i] > 0:
                gains.append(P[i+1] - P[i])
        
        return sum(gains)
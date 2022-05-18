class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        maxLeft = [0] * n
        maxRight = [0] * n
        
        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i+1])
        
        res = 0
        
        for i in range(n):
            minHeight = min(maxLeft[i], maxRight[i])
            if (minHeight > height[i]):
                res += minHeight - height[i]
        
        return res
            
            
            
        
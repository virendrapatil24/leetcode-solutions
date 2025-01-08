class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left = [0] * n
        right = [0] * n
        left[0], right[-1] = height[0], height[-1]

        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])
            right[n - 1 - i] = max(height[n - 1 - i], right[n - i])
        
        water = 0
        for idx, h in enumerate(height):
            water += min(left[idx], right[idx]) - h
        
        return water 

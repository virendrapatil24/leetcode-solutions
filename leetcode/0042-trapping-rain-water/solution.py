class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[-1] = height[-1]
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j])

        water = 0
        for k in range(1, n - 1):
            water += min(left_max[k], right_max[k]) - height[k]

        return water

        

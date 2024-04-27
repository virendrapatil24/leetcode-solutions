class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        l_max = [0] * n
        r_max = [0] * n

        l_max[0] = height[0]
        for i in range(1, n):
            if l_max[i-1] >= height[i]:
                l_max[i] = l_max[i-1]
            else:
                l_max[i] = height[i]
        
        r_max[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            if r_max[j+1] >= height[j]:
                r_max[j] = r_max[j+1]
            else:
                r_max[j] = height[j]

        for k in range(1, n-1):
            if l_max[k] <= r_max[k]:
                min_height = l_max[k]
            else:
                min_height = r_max[k]
            res +=  min_height - height[k]

        return res 
        

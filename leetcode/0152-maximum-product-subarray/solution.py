class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro, prefix, suffix = -inf, 1, 1
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n - 1 -i]
            max_pro = max(max_pro, max(prefix, suffix))
        return max_pro
        

        

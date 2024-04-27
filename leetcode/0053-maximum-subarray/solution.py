class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if max_sum + nums[i] > nums[i]:
                max_sum = max_sum + nums[i]
            else:
                max_sum = nums[i]
            if res < max_sum:
                res = max_sum
        return res        

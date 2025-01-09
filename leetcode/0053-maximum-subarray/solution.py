class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            res = max(res, max_sum)
        return res

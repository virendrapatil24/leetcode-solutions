class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        for i in range(n):
            start = max(0, i - nums[i])
            total_sum += sum(nums[start: i + 1])
        return total_sum
        

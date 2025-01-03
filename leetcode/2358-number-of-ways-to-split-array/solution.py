class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        curr_sum, total_sum = 0, sum(nums)
        n = len(nums)
        splits = 0
        for i in range(n - 1):
            curr_sum += nums[i]
            if curr_sum >= total_sum - curr_sum:
                splits += 1
        return splits
            

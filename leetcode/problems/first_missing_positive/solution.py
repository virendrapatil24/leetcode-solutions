class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if 1 in nums:
            x = nums.index(1)
        else: return 1
        
        for i in range(x+1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                return nums[i-1] + 1
            if i == len(nums)-1:
                return nums[i] + 1
        return 2
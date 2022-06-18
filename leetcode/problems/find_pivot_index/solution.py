class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum, rSum = 0, sum(nums)
        
        for idx, val in enumerate(nums):
        
            rSum -= val
        
            if lSum == rSum:
                return idx
        
            lSum += val
        
        return -1
        
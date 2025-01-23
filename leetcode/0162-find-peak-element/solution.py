class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) 
        if n == 1 or nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return n - 1

        l, r = 1, n - 2
        while l <= r:
            m = (l + r) // 2
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            
            if nums[m] > nums[m - 1]:
                l = m + 1
            else:
                r = m - 1
        
        return -1

        

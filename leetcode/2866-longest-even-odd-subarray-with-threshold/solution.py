class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = 1 if nums[0] % 2 == 0 and nums[0] <= threshold else 0
        curr = 1 if nums[0] % 2 == 0 and nums[0] <= threshold else 0
        n = len(nums)
        for i in range(1, n):
            if curr == 0:
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    curr = 1
            else:
                if nums[i] % 2 != nums[i-1] % 2 and nums[i] <= threshold and nums[i-1] <= threshold:
                    curr += 1
                elif nums[i] % 2 == 0 and nums[i] <= threshold:
                    res = max(curr, res)
                    curr = 1
                else:
                    res = max(curr, res)
                    curr = 0
        return max(curr, res)
        
            
        

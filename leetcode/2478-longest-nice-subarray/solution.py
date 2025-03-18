class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        curr = 0
        max_len = 1
        for r in range(len(nums)):
            while curr & nums[r]:
                curr = curr ^ nums[l]
                l += 1
            max_len = max(max_len, r - l + 1)
            curr = curr | nums[r]
        return max_len


        

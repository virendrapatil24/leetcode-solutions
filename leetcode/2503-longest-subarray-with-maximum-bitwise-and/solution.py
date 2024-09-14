class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = cur = mx = 0
        for num in nums:
            if num > mx:
                mx = num
                longest = cur = 0
            cur = cur + 1 if num == mx else 0
            longest = max(longest, cur)
        return longest
        

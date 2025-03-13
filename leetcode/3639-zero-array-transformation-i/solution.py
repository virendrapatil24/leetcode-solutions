class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        freq = [0] * len(nums)
        for l, r in queries:
            freq[l] += 1
            if r + 1 < len(nums):
                freq[r + 1] -= 1
        
        curr_freq = 0
        for i, num in enumerate(nums):
            curr_freq += freq[i]
            if curr_freq < num:
                return False
        return True

        

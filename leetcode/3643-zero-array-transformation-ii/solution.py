class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l, r = 0, len(queries)
        if not self.can_form_zero_array(nums, queries, r):
            return -1
        while l <= r:
            m = (l + r) // 2
            if self.can_form_zero_array(nums, queries, m):
                r = m - 1
            else:
                l = m + 1
        return l
    
    def can_form_zero_array(self, nums, queries, k):
        n = len(nums)
        freq = [0] * n
        for idx in range(k):
            l, r, val = queries[idx]
            freq[l] += val
            if r + 1 < n:
                freq[r + 1] -= val
        curr_freq = 0
        for i, num in enumerate(nums):
            curr_freq += freq[i]
            if curr_freq < num:
                return False
        return True
        

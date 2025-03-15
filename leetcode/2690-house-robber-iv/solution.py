class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 0, max(nums)
        while l <= r:
            m = (l + r) // 2
            if self.is_possible(nums, k, m):
                r = m - 1
            else:
                l = m + 1
        return l
        
    def is_possible(self, nums, k, capacity):
        n = len(nums)
        i = 0
        count = 0
        while i < n:
            if nums[i] <= capacity:
                count += 1
                i += 2
            else:
                i += 1
        return count >= k

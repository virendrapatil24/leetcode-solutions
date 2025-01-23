class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        res = max(nums)
        while l <= r:
            mid = (l + r) // 2
            if self.is_possible(nums, mid, threshold):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def is_possible(self, nums, divisor, threshold):
        curr_threshold = 0
        for num in nums:
            curr_threshold += ceil(num / divisor)
        
        return curr_threshold <= threshold

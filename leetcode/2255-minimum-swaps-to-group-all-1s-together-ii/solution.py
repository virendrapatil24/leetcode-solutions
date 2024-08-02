class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = 0
        for num in nums:
            ones += num
        x, ones_in_window = 0, 0
        n = len(nums)
        for i in range(n * 2):
            if i >= ones and nums[i % n - ones]: x -= 1
            if nums[i % n] == 1: x += 1
            ones_in_window = max(x, ones_in_window)
        return ones - ones_in_window

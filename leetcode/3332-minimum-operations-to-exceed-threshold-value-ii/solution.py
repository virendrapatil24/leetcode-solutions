class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ops = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            new_num = min(x, y) * 2 + max(x, y)
            heappush(nums, new_num)
            ops += 1
        return ops


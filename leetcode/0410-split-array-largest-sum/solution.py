class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        ans = sum(nums)
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m)
            if self.is_possible(nums, k, m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans

    def is_possible(self, nums, k, target):
        count = 1
        curr_sum = 0
        for num in nums:
            if num + curr_sum <= target:
                curr_sum += num
            else:
                count += 1
                curr_sum = num
        return count <= k
        

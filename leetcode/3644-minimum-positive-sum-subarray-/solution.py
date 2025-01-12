class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int: 
        min_sum = inf
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        for length in range(l, r + 1):
            for i in range(n - length + 1):
                curr_sum = prefix_sum[i + length] - prefix_sum[i]
                if curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)
        return min_sum if min_sum != inf else -1
        

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        nums_sum = sum(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        count = 0
        for i in range(n - 1):
            if (prefix_sum[i] - (nums_sum - prefix_sum[i])) % 2 ==0:
                count += 1

        return count
            
        

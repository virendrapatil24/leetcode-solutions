class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        hash_map = {}
        prefix_sum = 0
        max_len = 0
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum == 0:
                max_len = i + 1
            if prefix_sum in hash_map:
                max_len = max(max_len, i - hash_map[prefix_sum])
            else:
                hash_map[prefix_sum] = i
        return max_len

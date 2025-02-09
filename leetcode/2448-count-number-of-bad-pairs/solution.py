class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        slope_map = {}
        n = len(nums)
        for i in range(n):
            slope_map[nums[i] - i] = slope_map.get(nums[i] - i, 0) + 1
        
        good_pairs = 0
        for slope, count in slope_map.items():
            if count > 1:
                good_pairs += count * (count - 1) // 2
        
        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs

        

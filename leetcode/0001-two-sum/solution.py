class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_sum = {}
        for idx, num in enumerate(nums):
            if num not in map_sum:
                map_sum[target - num] = idx
            else:
                return [idx, map_sum[num]]


        

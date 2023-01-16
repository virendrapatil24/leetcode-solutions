class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target - num in nums and nums.index(target - num) != idx:
                return [idx, nums.index(target - num)]
        return -1
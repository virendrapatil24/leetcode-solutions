class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        return [left, right] if left < len(nums) and nums[left] == target else [-1, -1]
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el, count = nums[0], 1
        for i in range(1, len(nums)):
            if count != 0:
                count += 1 if nums[i] == el else -1
            else:
                el = nums[i]
                count = 1
        return el
        

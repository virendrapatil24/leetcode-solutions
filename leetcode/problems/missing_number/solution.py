class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        #if
        for i in range(0,nums[-1]):
            if i != nums[i]:
                return i
        return len(nums)
        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num > 0:
                nums_set.add(num)
        for i in range(1, len(nums)+2):
            if i not in nums_set:
                return i
        return -1
            
        

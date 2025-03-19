class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                for j in range(3):
                    nums[i + j] = 0 if nums[i + j] else 1
                count += 1
        return -1 if 0 in nums[-2:] else count


        

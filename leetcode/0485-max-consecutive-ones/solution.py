class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, curr_count = 0, 0
        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0
        max_count = max(max_count, curr_count)
        return max_count
        

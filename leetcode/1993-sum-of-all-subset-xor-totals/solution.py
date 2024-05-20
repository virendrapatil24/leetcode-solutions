class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def subset_xor_sum(arr, level, currentXOR):
            if level == len(arr):
                return currentXOR
            
            inc = subset_xor_sum(arr, level + 1, currentXOR ^ nums[level])

            exc = subset_xor_sum(arr, level + 1, currentXOR)

            return inc + exc
        
        return subset_xor_sum(nums, 0, 0)
        
